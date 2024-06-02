from function_list import print_models, show_completed_models
magicians = ["sam", "james", "jane", "jarvis", "daniel"]

def show_magicians(magicians):
    """Print names of magicians from a list."""
    for magician in magicians:
        print(magician.title())


print("----------------------------Exercise-2-------------------------------")


def make_great(magicians_list):
    new_magicians = []
    while magicians:
        current_magician = magicians_list.pop()
        new_magicians.append("Great " + current_magician)
        
        magicians_list = new_magicians
    
    print(magicians_list)



unprinted_designs = ["iphone case", "robot pendant", "dodecahedron"]
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)