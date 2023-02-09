from flask import Flask, request, send_from_directory
from flask_cors import CORS
from json import dumps, loads, load, dump
from dog import Dog

def defaultHandler(err):
    response = err.get_response()
    print('response', err, err.get_response())
    response.data = dumps({
        "code": err.code,
        "name": "System Error",
        "message": err.get_description(),
    })
    response.content_type = 'application/json'
    return response

APP = Flask(__name__)
CORS(APP)

@APP.route("/register", methods=['POST'])
def signup():
    """Retrieving data from a post request and creating a dog to store in data"""
    # Retrieving data from post request and creating a dog for that data to st
    payload = request.get_json()
    dog = Dog(payload["Name"], payload["age"], payload["suburb"], payload["breed"], payload["gender"], payload["photo"], payload["temperament"], payload["bio"], payload["email"], payload["name"])
    with open("data.json", "r+") as file:
        file_data = load(file)
        file_data["dogs"].append(dog.return_dog())
        file.seek(0)
        dump(file_data, file, indent=4)
    return dumps(dog.return_dog())

@APP.route("/login", methods=['POST'])
def login():
    """Logging in a user given their email and validating it with database"""
    payload = request.get_json()
    with open("src/data.json", "r+") as file:
        file_data = load(file)
        for dog in file_data["dogs"]:
            if dog['email'] == payload['email']:
                return dumps(dog["name"])

@APP.route("/getalldogs", methods=["GET"])
def getalldogs():
        """Return all the dogs stored in the database"""
        with open("data.json", "r+") as file:
            file_data = load(file)
            all_dogs = file_data['dogs']
        return dumps(all_dogs)

@APP.route("/get_image/<filename>", methods=["GET"])
def get_image(filename):
    return send_from_directory("pictures", filename)


@APP.route("/getallparks", methods=["GET"])
def getallparks():
        """Return all the parks stored in the database"""
        with open("data.json", "r+") as file:
            file_data = load(file)
            all_parks = file_data['parks']
        return dumps(all_parks)

    
    
    
    


if __name__ == "__main__":
    APP.run(port=8080)