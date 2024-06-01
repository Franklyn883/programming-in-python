# name = input("Enter your name: ")
# print("Hello " + name.strip().title() + "!")

#Exercise 
# prompt = "Your comfort is our number one priority..."
# prompt += "\nwhat car will you like! "

# car = input(prompt)
# print("Let me find you a "+ car)

# prompt = "Make a booking for your dinner!"
# prompt +="\nHow many people do you want to book for: "
# booking = input(prompt)

# if int(booking) > 8:
#     print("\nsorry, you will have to wait for a table")
    
# else:
#     print("\nyour table is ready")

prompt = "Enter a number "
number = input(prompt)
if (int(number) % 10 == 0):
    print(number + " is a multiple of 10")
else:
    print(number + " is not a multiple of 10")