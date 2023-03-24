#Scope in python
#global scope
#global_scope = 5
#def local_scope ():
#    #local scope
#    local_v = 10
#    print(global_scope)
#    print(local_v)
#    print(enclosed_V)
#    #enclosed scope
#    def enclosed_scope():
#      enclosed_v = 15
#      print(local_v)
#    
#    enclosed_scope()
#local_scope()

##DATA STRUCTURE
#Data Structure in python: This is all about organizing your data for easily manipulation
#There are various types: python's data structure and user's data structure
#for python: list,tuple,sets and dictionary, and we have user's defined data structure:
#Hashmap, tree, graph, queue, stack and linked list.

#List is just like an array in js. It's data are mutable. it can store any form of datatype.
list
#List
list1 = [1,2,3,4,5,6,7,8,9,10]
#access the values in the list
print(list1[5])
#to print the list
print(*list1)#prints it out without the bracket and commas
print(list1, sep=' ')
#adding values to the list
#using the insert method, you include the position and the value
list1.insert(len(list1), 11)
print(list1)
#using append you only include the value and it adds it to the end of the list values
list1.append(12)
print(list1)
#Extend can add multiple values to end of the list
list1.extend([13,14,15])
print(list1)
#deleting items from the list
#pop removes the value at a specified index
removed_items = list1.pop(14)
print(list1)
print(removed_items)
#using the del keyword
del list1[13]
print(list1)

