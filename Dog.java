public class Dog {
    private String name;
    private int age;
    private String breed;
    private String suburb;
    private String temperment;
    private String gender;
    private String bio;
    private String email;
    private String password;

    public Dog(String name, int age, String breed, String suburb, String temperment, String gender, String bio, String email, String password) {
    {
        this.name=name;
        this.age=age;
        this.breed = breed;
        this.suburb = suburb;
        this.temperment = temperment;
        this.gender = gender;
        this.bio = bio;
        this.email = email;
        this.password = password;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getBreed() {
        return breed;
    }

    public void setBreed(String breed) {
        this.breed = breed;
    }

    public String getSuburb() {
        return suburb;
    }

    public void setSuburb(String suburb) {
        this.suburb = suburb;
    }

    public String getTemperment() {
        return temperment;
    }

    public void setTemperment(String temperment) {
        this.temperment = temperment;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getBio() {
        return bio;
    }

    public void setBio(String bio) {
        this.bio = bio;
    }
}
