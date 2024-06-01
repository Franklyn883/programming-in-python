def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)


usernames = ["hannah", "jude", "james", "john", "samson"]

greet_users(usernames)

unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print("Printing model: " + current_design)
#     completed_models.append(current_design)

# print(completed_models)

print("\n---------------------Printing model--------------------------------\n")


def print_models(unprinted_designs, completed_models):
    """Stimulate printing each design, until none are left."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all models that are printed."""
    print("The following models has being printed: ")
    for model in completed_models:
        print(model)


print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
