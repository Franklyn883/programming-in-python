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