class Dog:
    def __init__(self, name, age, suburb, breed, gender, photo_path, temperament, bio, email, owner_name):
        self.name = name
        self.age = age
        self.suburb = suburb
        self.breed = breed
        self.gender = gender
        self.photo_path = photo_path
        self.temperament = temperament
        self.bio = bio
        self.email = email
        self.owner_name = owner_name

    def return_dog(self):
        return {
            "name": self.name,
            "age": self.age,
            "suburb": self.suburb,
            "breed": self.breed,
            "gender": self.gender,
            "photo": self.photo_path,
            "temperament": self.temperament,
            "bio": self.bio,
            "owner": self.owner_name,
            "email": self.email,
        }