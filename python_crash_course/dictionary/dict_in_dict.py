users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

for username, user_info in users.items():
    print("\nusername: " + username.title())
    full_name = user_info["first"].title() + " " + user_info["last"].title()
    location = user_info["location"]
    print("\tFull name: " + full_name)
    print("\tLocation: " + location)

# Exercise
people = {
    "peter": {
        "sex": "male",
        "marital_status": "married",
        "religion": "christian",
    },
    "favor": {
        "sex": "male",
        "marital_status": "single",
        "religion": "christian",
    },
}

for person, person_info in people.items():
    print("\n" + person.title())
    print("\tsex: " + person_info["sex"])
    print("\tmarital status: " + person_info["marital_status"])
    print("\treligion: " + person_info["religion"])

pets = {
    "ruby": {
        "type": "dog",
        "breed": "chiwawa",
        "color": "white",
        "owner": "john",
    },
    "lipsy": {
        "type": "cat",
        "breed": "foreign",
        "color": "black",
        "owner": "james",
    },
}

for pet, pet_info in pets.items():
    print("\n" + pet.title())
    type = pet_info["type"]
    breed = pet_info["breed"]
    color = pet_info["color"]
    owner = pet_info["owner"]
    print("\t type: " + type)
    print("\t breed: " + breed)
    print("\t color: " + color)
    print("\t owner: " + owner.title())
