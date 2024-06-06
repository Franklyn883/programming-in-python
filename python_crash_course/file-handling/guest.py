prompt = "Hello tell me your name: "
response = input(prompt)
filename = "/home/frank/repos/programming-in-python/python_crash_course/file-handling/guest.txt"

response = response.title() + "\n"
with open(filename, "a") as file_object:
    file_object.write(response)

with open(filename) as file_object:
    content = file_object.read()
    
    for line in content:
        line.replace("frrank","frank")
    