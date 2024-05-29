#tuple are just like list, the only difference is that
#they cant change.
dimensions = (200,50)
print(dimensions[0])
print(dimensions[0])

print("\nhere are the dimensions in my program:")
for dimension in dimensions:
    print(dimension)
    
#though you can't alter a tuple, you can reassign it.
print("\nOriginal dimension:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
    
#Exercise
print("\n-------------------Exercise-----------------------------\n")

buffets = ("beans and plantain", "fried-rice", "jollof rice", "bread", "porriage")

for buffet in buffets:
    print(buffet)
    
buffets = ("beans", "plantain", "fried-rice", "jollof rice", "pepper soup", "noodles")

print("\nnew list:")
for buffet in buffets:
    print(buffet)
    