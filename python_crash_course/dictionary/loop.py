# Looping through a dictionary is a common aspect of programming, python offers
# various way to achieve this
user_0 = {"username": "efermi", "first_name": "enrico", "last_name": "fermi"}
for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

for key in user_0:
    print(key)
    
for value in user_0.values():
    print(value)

print("\n")
for key in sorted(user_0.keys()):
    print(key)