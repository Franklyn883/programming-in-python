filename = "/home/frank/repos/programming-in-python/python_crash_course/file-handling/pi_digits.txt"

# with open(filename) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# #printing file content line by line
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
    
filename = "/home/frank/repos/programming-in-python/python_crash_course/file-handling/learning_python.txt"

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
    
    
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
     print(line.rstrip())
     
with open(filename, 'a') as file_object:
    file_object.write("I love python programming.\n")
    file_object.write("Python is the best programme out there.\n")
    file_object.write("I like that with programme i find fulfillment.\n")
    
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
     print(line.rstrip())