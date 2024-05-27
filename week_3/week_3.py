# ----------------------------------MAP AND FILTER FUNCTIONS-----------------------------------------------------------
# #Map is use to iterate over a list and returns both values that are true and not true. 
# # #It takes two argument: a function and a sequence
# menu = ['espresso', 'mocha', 'latte', 'cappuccino', "cortado", "americano"]
# # # #Here's a function that takes the items in the list and return only that's that starts with c
# def find_coffee (coffee):
#     if(coffee[0] =="c"):
#         return coffee
# # # #now we create a map function to run through the list and pass every item of the list through
# # # #the find_coffee function
# # map_coffee = map(find_coffee,menu)#this returns a map object we can display the content by simply
# # # #iterating over the list
# # print(map_coffee)
# # #output: <map object at 0x7f316e05ff10>
# # map_coffee_list = []
# # for x in map_coffee:
# #    map_coffee_list.append(x)
# # print(map_coffee_list)
# # #output: [None, None, None, 'cappuccino', 'cortado', None]

# #----------------Filter
# # #filter behaves the same way as map, only that it returns only values that are true.
# filter_coffee = filter(find_coffee, menu)
# # print(filter_coffee)
# filter_coffee_list = []
# for x in filter_coffee:
#    filter_coffee_list.append(x)
# print(filter_coffee_list)
# #output:['cappuccino', 'cortado']
#------------------------------------------------COMPREHENSION----------------------------------------------------------

# #comprehension is a way of creating a new sequences from an existing sequence.
#the syntax goes like this [ <expression> for x in <sequence> if <condition>] 

#-------------------------LIST COMPREHENSION
#Ex1: List comprehension: updating the same list
data = [2,3,5,7,11,13,17,19,23,29,31]
data = [x+3 for x in data]
#print("updating the list...",data)
#output: updating the list... [5, 6, 8, 10, 14, 16, 20, 22, 26, 32, 34]
# Ex2: List comprehension: creating a different list with updated values
new_data = [x*3 for x in data]
print('creating new list...', new_data)
#output: creating new list... [15, 18, 24, 30, 42, 48, 60, 66, 78, 96, 102]
# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x%4 == 0]
print('divisible by 4...', fourx)
#output: divisible by 4... [24, 48, 60, 96]
# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x%4==0]
print('divisible by four -1...',fourxsub)
#output: divisible by four -1... [23, 47, 59, 95]
# Ex5: Using range function:
nines = [x for x in range(100) if x%9 == 0]
print("multiples of nine...", nines)
#output: multiples of nine... [0, 9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 99]

#-------------------------DICTIONARY COMPREHENSION
#syntax dict = { key:value for key, value in <sequence> if <condition> } 
#Dictionary comprehension takes one or two lists as input and creates a dictionary out of it. I will now demonstrate 
# how this can be done using only one list and by using two lists. 

# # #using range
# using_range = {x:x*2 for x in range(12)}
# print('using range...', using_range)
# #output: using range... {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18, 10: 20, 11: 22}
# # # Lists
# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]
# # #using one input list
# num_dict = {x:x**2 for x in number}
# print('using one input list to create dictionary...', num_dict)
# #output: using one input list to create dictionary... {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64,
# #  9: 81, 10: 100, 11: 121, 12: 144}
# # #using two list
# # #in the case of using two list the format is: --new_dict ={key:value for (key, value) in zip(list1, list2)}--
# months_dict ={key:value for (key,value) in zip(number, months)}
# print('using two lists...', months_dict)
# #outputusing two lists... {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June', 7: 'July', 8: 'Aug',
# #  9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}


#---------------SET COMPREHENSION
# The set comprehension deals with the set data type and it's very similar to list comprehension.
# The only key difference is the use of curly brackets for sets instead of square brackets as in lists. For example:
# set_a = {x for x in range(10,20) if x not in [12,14,16]}
# print("list of items between 10 to 20, except 12, 14, and 16....", set_a)
# #output list of items between 10 to 20, except 12, 14, and 16.... {10, 11, 13, 15, 17, 18, 19}


#--------------------GENERATOR COMPREHENSION
# #Generator comprehensions are also very similar to lists with the variation of using curved brackets 
# # instead of square brackets. They are also more memory efficient as compared to list comprehensions. For example:
# data = [2,3,5,7,11,13,17,19,23,29,31]
# gen_obj =(x for x in data)
# #print(gen_obj)#this returns an object
# #we have to iterate through to get the values
# for x in gen_obj:
#     print(x, end=" ")
#    #output:2 3 5 7 11 13 17 19 23 29 31


# #------------------Difference between map() and comprehension
# data = [2,3,5,7,11,13,17,19,23,29,31]
# new_data = [x*2 for x in data]
# #first a function to return X2 of the data items
# def num_x2(num):
#     return num*2

# map_data =map(num_x2,data)
# new_map_data = []
# for x in map_data:
#    new_map_data.append(x)


# print(new_data)
# print(new_map_data)
# a = [[96], [69]]

# # print(''.join(list(map(str, a))))
# # z = ["alpha","bravo","charlie"]
# # new_z = [i[0]*2 for i in z]
# # print(new_z)
# # Input data: List of dictionaries
# employee_list = [
#    {"id": 12345, "name": "John", "department": "Kitchen"},
#    {"id": 12456, "name": "Paul", "department": "House Floor"},
#    {"id": 12478, "name": "Sarah", "department": "Management"},
#    {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
#    {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
#    {"id": 12419, "name": "Gill", "department": "Cashier"}
# ]
# initial = []
# id = []
# for employee in employee_list:
#       initial.append(employee['name'][0])

   
# for employee in employee_list:
#       id.append(employee['id'])

# print(initial)
# print(id)

# # Function to be passed to the map() function. Do not change this.
# def mod(employee_list):
#    temp = employee_list['name'] + "_" + employee_list["department"]
#    return temp

# def to_mod_list(employee_list):
#    """ Modifies the employee list of dictionaries into list of employee-department strings

#    [IMPLEMENT ME] 
#       1. Use the map() method to apply mod() to all elements in employee_list

#    Args:
#       employee_list: list of employee objects

#    Returns:
#       list - A list of strings consisting of name + department.
#    """
#    ### WRITE SOLUTION CODE HERE
#    map_employee = map(mod,employee_list)
#    mod_list = []
#    for x in map_employee:
#      mod_list.append(x)
#    return mod_list
#    raise NotImplementedError()
# print(to_mod_list(employee_list))
# mod_list = to_mod_list(employee_list)

# def generate_usernames(mod_list):
#    """ Generates a list of usernames 

#    [IMPLEMENT ME] 
#       1. Use list comprehension and the replace() function to replace space
#          characters with underscores

#       List comprehension looks like:
#       list = [ function() for <item> in <list> ]

#       The format for the replace() function is:

#       test_str.replace(“a”, “z”) # replaces every “a” in test_str with “z”

#    Args:
#       mod_list: list of employee-department strings

#    Returns:
#       list - A list of usernames consisting of name + department delimited by underscores.
#    """
#    ### WRITE SOLUTION CODE HERE
#    com_mode_list = [x.replace(' ',"_") for x in mod_list]
#    return com_mode_list
#    raise NotImplementedError()
# print(generate_usernames(mod_list))
# def map_id_to_initial(employee_list):
#    """ Maps employee id to first initial

#    [IMPLEMENT ME] 
#       1. Use dictionary comprehension to map each employee's id (value) to the first letter in their name (key)

#       Dictionary comprehension looks like:
#       dict = { key : value for <item> in <list> }

#    Args:
#       employee_list: list of employee objects

#    Returns:
#       dict - A dictionary mapping an employee's id (value) to their first initial (key).
#    """
#    initial = []
#    id = []
#    for employee in employee_list:
#       initial.append(employee['name'][0])
#    for employee in employee_list:
#       id.append(employee['id'])
#    id_initial = {key:value for (key,value) in zip(initial,id)}
#    return id_initial

# print(map_id_to_initial(employee_list))

# def sum(n):
#    if n == 1:
#        return 0
#    return n + sum(n-1)

# a = sum(5)
# print(a)