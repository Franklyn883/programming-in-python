#if statements are used to test the logic of programmes
cars = ["audi", "bmw", "toyota", "honda", "tesla"]

print("\nlist of my favorite cars:")
for car in cars:
    if (car=="bmw"):
        print(car.upper())
    else:
        print(car.title())
        
usernames = ["favour", "james", "John", "Peter"]

if("jude" in usernames):
    print("name already exist, try again!")
else:
    print("user registered successfully!")
    
banned_user = ["grace", "julius", "sandra", "sarah"]

user = "grace"
if user not in banned_user:
    print("login successful!")
else:
    print("user is banned")
        

        
        
#numerical comparison
answer = 42

if answer !=42:
    print("That is the wrong answer, try again!")

else:
    print("Correct answer!")

