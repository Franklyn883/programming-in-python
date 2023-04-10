# '''
# pytest is the one of the framework for writing test in python
# '''
# def add(a,b):
#     return a + b

# def sub(a,b):
#     return  a - b
 

sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)

def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11)
names = ["Anna", "Natasha", "Mike"]
names.insert(2, "Xi")
print(names)
