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

##List is just like an array in js. It's data are mutable. it can store any form of datatype.
#list
##List
#list1 = [1,2,3,4,5,6,7,8,9,10]
##access the values in the list
#print(list1[5])
##to print the list
#print(*list1)#prints it out without the bracket and commas
#print(list1, sep=' ')
##adding values to the list
##using the insert method, you include the position and the value
#list1.insert(len(list1), 11)
#print(list1)
##using append you only include the value and it adds it to the end of the list values
#list1.append(12)
#print(list1)
##Extend can add multiple values to end of the list
#list1.extend([13,14,15])
#print(list1)
##deleting items from the list
##pop removes the value at a specified index
#removed_items = list1.pop(14)
#print(list1)
#print(removed_items)
##using the del keyword
#del list1[13]
#print(list1)

##Tuples are just like list, they can hold any datatype, the only difference is; tuple is immutable
#my_tuple = (1,'string',4,5,True)
##To access a value we use the index value
#print(my_tuple[2])
##count keyword is use to check the number of occurence
#print(my_tuple.count("string"))
##to check the index of a value
#print(my_tuple.index(5))

##SET is another datatype it different from list in that they don't duplicate value
#set_a = { 1, 2,3,4,5}
#print(set_a)
##set methods
##add:adds values to the set
#set_a.add(6)
#print(set_a)
##Update: to add multiple values to the set at same time
#set_a.update(3,4,5,5)
##Discard/remove: removes values from the set
#set_a.remove(5)
#print(set_a)
##union:Joins to sets together and inputting just one value incase of any duplicate
#set_b = {4,5,6,7,8,9,10}
#set_c = set_a.union(set_b)#same as set_a | set_b
#print(set_c)
##intersection: Shows value that are present in both sets
#set_d = set_a.intersection(set_b)# same as set_a $ set_b
#print(set_d)
##difference:shows element present in one set and not in the other set
#set_e = set_a.difference(set_b)# same as set_a - set_b
#print(set_e)
##symmetric_difference: shows values that are not present in both
#set_f =set_a.symmetric_difference(set_b) #same as set_a ^ set_b
#print(set_f)

#Dictionary is just like object in js, values can be accessed based on key:value pair. It is mutable
#sample_dict ={1:"coffee", 2:"tea", 3:"Juice", 4:"beverages", 5:"malta"}
##Accessing the value
#print(sample_dict[1])
##updating a value
#sample_dict[1] ="Vodka"
#print(sample_dict)
##deleting a value
#del sample_dict[3]
#print(sample_dict)
##iterating through the dictionary.
#for x in sample_dict:#this only gives the name without the value
#    print(x)
#
##prints keys and value
#for key, value in sample_dict.items():
#    print(str(key) +":" + value)
#
###ARGS and KWARGS(keyword ARGS)
#def sum(a,b):
#    return a+b
##print(sum(3,5,4))#trying to pass more arguments causes errors, with args will can pass multiple amount of args
#def sum_all(*args):
#    sum = 0
#    for x in args:
#        sum +=x
#    return sum
#print(sum_all(2,3))
#
###KWARGS is similar to ARGS but allows key:values pairs
#def sum_kwargs(**Kwargs):
#    sum = 0
#    for key, value in Kwargs.items():
#        sum +=value
#    return sum
#print(sum_kwargs(rice=12,beans=12,house_rent=24))
#
##choosing a data structure
#employee_list = [{"id": 12345, "name": "John", "department": "Kitchen"}, {"id": 12458, "name": "Paul", "department": "House Floor"}]
#
#def get_employee(id): 
#    for employee in employee_list:
#        if employee['id'] == id:
#            return employee
#
#print(get_employee(12458))
#employee_dict = {
#    12345: {
#        "id": "12345",
#        "name": "John", 
#        "department": "Kitchen"    
#    },
#    12458: {
#        "id": "12458",
#        "name": "Paul", 
#        "department": "House Floor"    
#    }
#}
#print()
#def get_employee_detail(id):
#    return employee_dict[id]
##print(get_employee_detail(12458))
#
#
#menu = {
#    1: {"name": 'espresso',
#        "price": 1.99},
#    2: {"name": 'coffee', 
#        "price": 2.50},
#    3: {"name": 'cake', 
#        "price": 2.79},
#    4: {"name": 'soup', 
#        "price": 4.50},
#    5: {"name": 'sandwich',
#        "price": 4.99}
#}
#order_list = [{'name':"coke", "price":2.5}, {'name':"soup", "price":4.50},{'name':"beverages", "price":5.50}]
#
#def calculate_subtotal(order):
#    items_sum = 0
#    for items in order:
#        items_sum += items["price"]
#    return round(items_sum,2)
#print(calculate_subtotal(order_list))
#def calculate_tax(subtotal):
#    
#    tax = (15*subtotal)/100
#    return round(tax,2)
#subtotal = calculate_subtotal(order_list)
#print(calculate_tax(subtotal))
#
##Implement summarize_order() which returns a list of the names of the items
##that the customer ordered and the total amount (including tax) that they have to pay.
##The orders should show the name and price.
#def summarize_order(order):
#    total =calculate_tax(subtotal) + calculate_subtotal(order)
#    name = []
#    for item in order:
#        name.append(item['name'])
#    print('you bought:'+  str(name) +"your total bill is:" + str(total))
#    return round(total,2), name
#print(summarize_order(order_list))

## File handling in python
#opening a file and reading it in python
#file = open('week_2/text.txt', mode="r")
#data = file.readline()#this is used to read a single line
#print(data)
#file.close()#to close the file
#print(data)
##another way is with the "with" function. it closed the file automatically
#with open("week_2/text.txt", mode="r") as file:
#    data = file.readline()
#    print(data)
#
###creating a file 
#try:
#    with open('sample/newfile.txt', 'a') as file:
#        file.writelines(['\nThis is a new file2',"\nThis is another line"])
#except FileNotFoundError as e:
#    print("ERROR",e)
#
###writng a programming to randomly generate names for a dog
#
#with open('pet_names.txt', 'w') as file:
#    file.writelines(["Ace","\nAtlas","\nBailey","\nBear","\nBlaze","\nBoomer","\nBuddy" \
#                     "\nCoco", "\nCooper", "\nDuke"])
#   
#with open('pet_names.txt', 'r') as file:
#   data = file.read()
#   #to turn the data into a list
#   data_list = data.split('\n')
#   print(data_list)
#   #now we can import a random math method to randomly generate a pet name for us.
#   import random
#   print(random.choice(data_list))

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, 'r') as file:
        file_content = file.readlines()
        file_list = []
        for x in file_content:
            file_list.append(x)
        print(file_list)
        return file_list
        
       
    raise NotImplementedError()
read_file_into_list('week_2/text.txt')

def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    file = open(file_contents, 'r')
    first_line = file.readlines()
    #to write a new file
    with open(output_filename, 'w') as file:
        file.write(first_line)
    with open(output_filename, 'r') as file:
     print(file.read())
    
   
write_first_line_to_file("week_2/text.txt", "newtext.txt")