# we can use a dictionary to store similar objects

favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}

print(
    "Sarah's favorite language is " + favorite_languages["sarah"].title() + "."
)
person = {
    "first_name": "Favour",
    "last_name": "Iyoha",
    "age": 31,
    "city": "Idunwele-Ewu",
}
print(person)
print(
    "Hello! my name is "
    + person["first_name"].title()
    + " "
    + person["last_name"].title()
    + ". I am "
    + str(person["age"])
    + " years old. I live in "
    + person["city"].title()
    + "."
)

favorite_numbers = {
    "jane": 10,
    "favour": 5,
    "peter": 15,
    "sandra": 20,
    "james": 25,
}
print("\n Jane's favorite number is: " + str(favorite_numbers["jane"]))
print("\n Favour's favorite number is: " + str(favorite_numbers["favour"]))
print("\n Peter's favorite number is: " + str(favorite_numbers["peter"]))
print("\n Sandra's favorite number is: " + str(favorite_numbers["sandra"]))
print("\n James's favorite number is: " + str(favorite_numbers["james"]))

glossary = {
    "list": "a collection of data",
    "tuple": "a collection of whose content can't be altered ",
    "conditional statement": "this are used to test a condition that evaluates \
    to either true of false",
    "method": "this a function that is related to a class.",
    "parameters": "these are the values pass to a function",
    "dictionary": "These a collection of data using a key-value pair",
    "title": "This is a method for transforming a string to a title case",
    "set": "This is a collection of data, that holds only one occurrence \
    of a value",
    "loop": "This is a programming feature, that helps run repetitive task",
}

for word, meaning in sorted(glossary.items()):
    print("\n" + word + ": " + meaning)

rivers = {
    "nile": "egypt",
    "niger": "nigeria",
    "jordan": "israel",
}

for river, country in rivers.items():
    print(river.title() + " runs through " + country + ".")
    
for river in rivers.keys():
    print(river.title() + " river.")
    
for country in rivers.values():
    print(country.title())
