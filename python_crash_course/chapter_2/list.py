'''List is the collection of items in a particular order.'''
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = "My first bicycle was a "+ bicycles[0].title() + "."
print(bicycles)
print(bicycles[0].title())
print(message)

#-----Exercise
print("\n----------------------------Exercise---------------------\n")
names = ["Favour", "Peter", "Junior", "Samuel"]
print("Hello "+names[0]+", How are you doing today?")
print("Hello "+names[1] + ", How are you doing today?")
print("Hello " + names[2] + ", How are you doing today?")

#Modifying a list: this is almost the same as modifying a variable.
print("\n------------------------------------Example-2---------------------\n")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0]='ducati'
print(motorcycles)

#Adding new items to a list using Appending
print("\n----------------------Append--------------------------\n")
motorcycles.append("honda")
print(motorcycles)

motorcycles = []
motorcycles.append("ducati")
motorcycles.append('yahama')
motorcycles.append('suzuki')
motorcycles.append('honda')
print(motorcycles)

#deleting items from list
print("\n---------------------deleting items from a list-------------\n")
#using 'del', it removes the item permanently without returning any values
del motorcycles[0]
print(motorcycles)

#using 'pop', it removes items from the list but returns the value, so you can do something with it if you wish.
popped_motorcycles = motorcycles.pop()
print(motorcycles,popped_motorcycles)

last_owned = motorcycles.pop()
print("My last owned motorcycle is " + last_owned)

motorcycles = ['ducati', 'yahama', 'suzuki', 'honda']

first_motorcycle = motorcycles.pop(0)
print("My first owned motorcycles is a "+ first_motorcycle.title())

#the third way to remove item from a list is using "remove",
#we can use this method if we don't know the position of the value we want to remove

print(motorcycles)
removed_motocycle= motorcycles.remove('yahama')
print(motorcycles)

print("\n------------------Exercise 3---------------------------\n")

guest_list = ["favour","peter","junior","monday"]
print("Hello " + guest_list[0].title() + ", I want to invite you to my birthday party!")
print("Hello " + guest_list[1].title() + ", I want to invite you to my birthday celebration!!")
print("Hello " + guest_list[2].title() + ", I want to invite you to my birthday celebration!!!")
print("Hello " + guest_list[3].title() + ", I want to invite you to my birthday celebration!!!")

print(guest_list)
print(guest_list[-1].title()+ ", sorry he won't make it!")
guest_list[-1]="emmanuel"
print(guest_list)

#we can use the insert keyword to add items to any position in our list

guest_list.insert(0,"james")
guest_list.insert(3, "samuel")
guest_list.append('tina')
print(guest_list)

print("\n-----------------------------Sorting a list ------------------\n")

#the sort method changes the position of the items on the list permanently.
cars = ['bmw', 'audi', 'toyoto', 'subaru','hyudai', 'mercedez']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


#we can also sort the list temporally by using the sorted method
print("Here is the original list")
print(cars)
print("\nHere is the the sorted list")
print(sorted(cars))
print("\nHere is the original list")
print(cars)

#reverse method:this can be use to sort list in a reverse order.
#It doesnt follow alphabetical order, but simple reverse the order

print("\n This is a reverse order ")
cars.reverse()
print(cars)
print(len(cars))

print("\n\n--------------------Exercise 4----------------\n")

locations = ['toronto', 'frances', 'london', 'turkey', 'usa']
print(locations)
print('\n sorted list:')
print(sorted(locations))
print("\n original list:")
print(locations)
print("\n reversed list:")
locations.reverse()
print(locations)
locations.reverse()
print(locations)

print("\n sorted list using the permanent method:")
locations.sort()
print(locations)
print("\n sorted list in reverse order")
locations.sort(reverse=True)
print(locations)

animals = ['lion','horse','goat', 'fowl', 'grasscutter']
print(animals[4])
