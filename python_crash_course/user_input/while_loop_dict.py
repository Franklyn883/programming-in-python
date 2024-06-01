unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title() + "...")
    confirmed_users.append(current_user)
    
print(confirmed_users)

# Removing all instance of a value in a list

pets = ["cats", "dogs", "cats", "cats", "hamster"]

while "cats" in pets:
    pets.remove("cats")
    
print(pets)
