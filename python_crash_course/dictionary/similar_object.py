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
}
print("\nList: "+glossary["list"])
print("\nTuple: "+glossary["tuple"])
print("\nConditional statement: "+glossary["conditional statement"])
print("\nMethod: "+glossary["method"])
print("\nParameters: "+glossary["parameters"])