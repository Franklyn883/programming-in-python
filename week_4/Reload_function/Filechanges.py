import os
contents = os.listdir(r"/home/frank/repos/programming-in-python/week_4/Reload_function")
print(contents)#this printout the current content of the directory
def print_changes():
    print("current directory contents: ")
    print(contents)