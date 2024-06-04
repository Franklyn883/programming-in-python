from collections import OrderedDict

glossary = OrderedDict()
glossary["list"] = "a collection of data."
glossary["tuple"] = "a collection of whose content can't be altered."
glossary["conditional statement"] = (
    "this are used to test a condition that \
evaluates to either true of false"
)
glossary["method"] = "this a function that is related to a class."
glossary["parameters"] = "these are the values pass to a function."
glossary["dictionary"] = "These a collection of data using a key-value pair."
glossary["title"] = (
    "This is a method for transforming a string to a title case."
)
glossary["set"] = (
    "This is a collection of data, that holds only one occurrence\
    of a value"
)
glossary["loop"] = (
    "This is a programming feature, that helps run repetitive task."
)

for word, meaning in glossary.items():
    print("\n" + word + ": " + meaning)
