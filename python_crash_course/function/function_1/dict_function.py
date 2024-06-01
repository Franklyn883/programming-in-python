def build_person(first_name, last_name, middle_name="", age=""):
    """Return an information about a person, in a dictionary"""
    person = {"first name": first_name, "last name": last_name}
    if middle_name:
        person["middle name"] = middle_name
    if age:
        person["age"] = age
    return person


person_1 = build_person("John", "Doe", "rick", 35)
print(person_1)
