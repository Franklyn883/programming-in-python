#Map and Filter functions
#Map is use to iterate over a list and returns both values that are true and not true. 
#It takes two argument: a function and a list or any other collections
menu = ['espresso', 'mocha', 'latte', 'cappuccino', "cortado", "americano"]
#Here's a function that takes the items in the list and return only that's that starts with c
def find_coffee (coffee):
    if(coffee[0] =="c"):
        return coffee
#now we create a map function to run through the list and pass every item of the list through
#the find_coffee function
map_coffee = map(find_coffee,menu)#this returns a map object we can display the content by simply
#iterating over the list
print(map_coffee)
for x in map_coffee:
    print(x)

#filter behaves the same way as map, only that it returns only values that are true.
filter_coffee = filter(find_coffee, menu)
print(filter_coffee)
for x in filter_coffee:
    print(x)
