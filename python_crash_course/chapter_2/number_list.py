#we can create a list for numbers

for value in range(1,10+1):
    print(value)
    
number_lists= list(range(1,21))
print(number_lists)

for number in number_lists:
    print(number)
    
even_numbers = list(range(2,21,2))
print(even_numbers)

multiply_of_4 = list(range(4,60,4))
print(multiply_of_4)

squares = []

for value in range(1,11):
    squares.append(value**2)
    print(str(value) + "^2 :" + str(value**2))
print(squares)

#------------Number lists methods--------------------

print("\n----------------------------number list mthods----------------\n")

print(min(squares))
print(max(squares))
print(sum(squares))

#List comprehension

squares = [value**2 for value in range(1,11)]
print(squares)

print("\n---------------------Exercise --------------------------------\n")

number_lists = []

for value in range(1,21):
    number_lists.append(value)
    
print(number_lists)

number_lists = [ value for value in range(1,1000001)]

#for value in number_lists:
    #print(value)
    
print("minimum number:",min(number_lists))
print("maximum number:",max(number_lists))
print("total sum:",sum(number_lists))

odd_numbers = list(range(1,21,2))

for value in odd_numbers:
    print(value)
    
multiple_of_3 = list(range(3,31,3))
print("\n---------Multiple of 3-------------")
for value in multiple_of_3:
    print(value)


number_cubes = []

print("\n-----------------cubes of 3----------------")

for value in range(1,11):
    number_cubes.append(value)
    print(str(value)+"^3:" + str(value**3))
    
com_number_cubes = [value**3 for value in range(1,11)]
print(com_number_cubes)