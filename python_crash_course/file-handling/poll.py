filename = "/home/frank/repos/programming-in-python/python_crash_course/file-handling/poll.txt"
while True:
    """Simple poll to get answers from various users. The prefix p represent the prompt."""
    print("spare some time for a little survey: ")
    p_name = input("What's your name ")
    with open(filename, "a") as file_object:
        file_object.write(p_name.title() + ": \n")
    p_programming_language = input("What's your best programming language")
    with open(filename, "a") as file_object:
        file_object.write("\t" + p_programming_language.title() + "\n")
    p_reason = input("Tell me why you love your programming language.")
    with open(filename, 'a') as file_object:
        file_object.write("\t" + p_reason + "\n\n")
    quit = input("Thanks your your response, enter 'q' to quit.")
    if quit == "q":
        break
