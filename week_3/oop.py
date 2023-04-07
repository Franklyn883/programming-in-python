# # #python uses Object oriented programming as a paradigm. OOP relays heavily on simplicity 
# # #and reusability to improve workflow # paradigm simply means style of writing codes.
# # #OOP relays on components such as: class, objects and methods to achieve it aims.


# #---------------------------CLASS-----------------------------------------
# #declaring a class
# class MyClass:
#     #pass #this is to tell python that this is an empty class, but we will do something
#           #with it later, else it throws an error.
#    # print('hello world')
#    a = 5
#    def sayHello(self):#inorder for the child class to be able to access this method reference
#                       #we need to pass a self argument to the method. You can use any other word. But self is 
#                        # just a convention. self points to the instance of the class
#       return "Hello i am a method of MyClass"
# myclass = MyClass()# this is to instantiate an object of the MyClass. So this is a child
#                   # and has access to the attributes(variables) and behavior reference of
#                   #the class
# print(myclass.a)#myclass has access to the attribute reference of the a variable.
# #output: 5
# print(myclass.sayHello())#the subclass myclass can also access the method
# #output Hello i am a method of MyClass

# #Examples
# # class House:
# #    '''
# #    This is a stub for a class representing a house that can be used to create an object and
# #    evaluate different metrics the we may require in constructing it.
# #    '''
# #    num_rooms = 5
# #    bathrooms = 2
# #    def cost_evaluation(self,rate):#we can pass in any number of arguments, but first one is 
# #                                   #always a reference to the instance of the class
                                
# #       cost = rate *self.num_rooms
      
# #       return cost
# #    #functionality to calculate the costs from the area of the house.
# # #we can call this class directly or instantiate an object of the class
# # house = House()
# # print(house.bathrooms)
# # print(House.bathrooms)
# # #now lets update the value of the child class
# # house.bathrooms = 7
# # print(house.bathrooms)#this changes
# # print(House.bathrooms)#but this still remains the same.
# # House.bathrooms = 5#change of the parent attribute no longer affect the obj.
# # print(house.bathrooms)
# # print(House.bathrooms)
# # House.num_rooms = 7#This affects it because the object does not have it's own defined num_room
# # print(house.num_rooms)
# # #now let call the method
# # print(house.cost_evaluation(100))

# # #----------------INSTANTIATE A CUSTOM OBJECT------------------
# # #Code reusability is a big part of OOP, being able to write a piece of code and reuse it at different instance to
# # #generate different results is the flex of OOP. OOP can create custom Object using Two methods.

# # # class Recipe():
# # #    '''
# # #    There are two method of creating a custom object
# # #    '''
# # #    #new method
# # #    def __new__(cls) -> Self:
# # #       pass
# # #    #the init method takes obj created with new method along with other arguments to instantiate the new 
# #       object being created
# # #    def __init__(self) -> None:#the self keyword stand as the self reference to the new object created. 
# #                                  Just like "this" keyword in js
# # #                               

# # #Example
# # class Recipe():
# #    def __init__(self,dish,items,time) -> None:#Here is a template of our new object
# #       self.dish = dish
# #       self.items = items
# #       self.time = time

# #   #lets create a method that will read out the string and tells us how long it will take to prepare a dish
# #    def contents(self):
# #       print('The ' + self.dish + " has " + str(self.items) + " and takes " + str(self.time)+ \
# #             " minutes to prepare")

# # #We can create instances of this object
# # pizza = Recipe('Pizza', ["cheese","bread", "tomatoes"], 45)
# # pasta = Recipe('Pasta', ["penne", "sauce"], 30)
# # egg_sauce = Recipe('Egg Sauce', ['eggs', "tomatoes", "pepper", "onions"], 15)
# # print(pizza.items)
# # #output: ['cheese', 'bread', 'tomatoes']
# # print(pasta.items)
# # #output:['penne', 'sauce']
# # print(egg_sauce.items)
# # #output: ['eggs', 'tomatoes', 'pepper', 'onions']
# # pizza.contents()
# # #output: The Pizza has ['cheese', 'bread', 'tomatoes'] and takes 45 minutes to prepare
# # pasta.contents()
# # #output: The Pasta has ['penne', 'sauce'] and takes 30 minutes to prepare
# # egg_sauce.contents()
# # #output: The Egg Sauce has ['eggs', 'tomatoes', 'pepper', 'onions'] and takes 15 minutes to prepare

# # class MyFirstClass():
# #     print("Who wrote this?")
# #     index = "Author-Book"

# #     def hand_list(self, philosopher, book):
# #         print(MyFirstClass.index)
# #         print(philosopher + " wrote the book: " + book)

# # whodunnit = MyFirstClass()
# # whodunnit.hand_list("Sun Tzu", "The Art of War")

# # #--------------------INSTANCE METHODS--------------
# # #This class creates an instance that can be used to check if an employee has being paid or not.
# # class Pays_slip:
# #     def __init__(self,name,payment,amount) -> None:
# #         self.name = name
# #         self.payment = payment
# #         self.amount = amount
# # #the method updates the payment status
# #     def pay(self):
# #         self.payment = "yes"
        
# #     def status(self):
# #         if self.payment == "yes":
# #             return self.name + " is paid " + str(self.amount)
# #         else:
# #             return self.name + " is not paid yet"

# # #lets instantiate an object off the class
# # nathan = Pays_slip('Nathan', "no" , 1000)
# # print(nathan.status())
# # nathan.pay()#
# # print("After")
# # print(nathan.status())
# # jonas = Pays_slip("Jonas", "no", 500)
# # print(jonas.status())

# #-------------------Parent class vs Child Classes------------------------------------
# #super class
# class Employees:
#     def __init__(self, name,last) -> None:
#         self.name = name
#         self.last = last

# #This is inheritance in practice.
# #subclass
# class Supervisors(Employees):#It inherit all the 
#     def __init__(self, name, last, password) -> None:#added property
#         super().__init__(name, last)#the inherited property
#         self.password = password

# class Chefs(Employees):
#     def leave_request(self, days):
#         return self.name +" " + self.last + " Requesting for " + str(days) + "days of leave"
    
# adrian = Employees("Adrian", "K")
# emily = Supervisors('Emily',"J","apple")
# jerry = Chefs("Jerry",".K" )
# #print(jerry.last)
# print(jerry.leave_request(10))
# #output: Jerry .K Requesting for 10days of leave

# #-----------------------INHERITANCE
#------------simple inheritance: the inheritance is just in a single level
# class A: #class A is the parent class
#     pass
# class B(A):#class B is the child class and inherits the attributes and behaviors of class A
#     pass

# #----------------MULTIPLE INHERITANCE
# class A:#first this super class
#     a = 1
# class B:#A super class
#     b = 2
# class C(A,B):#class c inherits from both class A,  and class B
#     pass
# c = C()#instantiate an object c that inherits from the class C, which intone inherited it's properties from class A and B
# print(c.a)
# #output: 1
# print(c.b)
# #output: 2

# #-------------MULTI-LEVEL INHERITANCE
# class A:    
#     a = 1    
# class B(A):
#     a = 2   
# class C(B):
#     pass
# c = C()
# print(c.a)  #the out put will be 2 because c inheritance is directly from Class C, which inherited from class B


# #-------------------BUILT-IN FUNCTIONS
# '''
# There are two useful function use to check the inheritance in python. The issubclass()  and isinstance()function
# issubclass(): it takes two classes as arguments. it checks if the first class is a child of the second class. 
#               Then return true or false based on the result.

# '''
# print(issubclass( A,B))#This will return False because A is not a subclass of B
# #output: False
# print(issubclass(B,A))#this will return True because B is a subclass of A

# '''
# isinstance(): it works the same way as issubclass(),but determines if an object is an instance of a class.

# '''
# print(isinstance(c, C))#this this returns True, because c is an instance of the class C.

#-------Super():
# '''
# Super() function is a built-in function that can be called inside the derived class and give access to the methods
# and variables of the parent classes or siblings. When you call the super() function, you get an object that 
# represent the parent class in return.
# '''
# class Fruit():
#     def __init__(self, fruit) -> None:
#         print('Fruit type: ' ,fruit)

# class FruitFlavour(Fruit):
#     def __init__(self) -> None:
#         super().__init__("Apple")#this is use to initialize the base class in side the child class so it get access to
#                                 #the method.
#         print("Apple is sweet")

# apple = FruitFlavour()
# #output:Fruit type:  Apple
# #output: Apple is sweet

#--------------------METHOD RESOLUTION ORDER---------------------------------------------
'''
In the case where there is multiple inheritance. MRO helps to resolve the issues of inheritance conflicts.
there are four major types of inheritance:
i.simple inheritance: Just a parent -> child inheritance.
ii.multiple inheritance: this is when a child class inherit from different parents.
iii.multi-level inheritance: this is when inheritance happens in multiple levels. like a child inheriting from a subclass
that subclass inheriting from other parents. The chain can go on and on
iv.Hierarchical inheritance: this handles how several subclass inherit from one and other.
There is a fifth type called HYBRID-INHERITANCE which combines the characters from the other types of inheritance.
MRO: It determines the order a given method or attribute is passed through in a search ot the hierarchy of classes for 
 it's resolution. The order of resolution is 
called LINEARIZATION OF A CLASS. it follows a simple logic bottom to top, left to right. The older version of python
uses a DEPTH-FIRST SEARCH ALGORITHM(DFS) while recent version use C3 LINEARIZATION ALGORITHM.
MRO() FUNTIONS:There are two functions to check the inheritance of class :
mro(): shows the inheritance graph of the classes
help(): Provides more details with the mro() information at the top
''' 
#Example    
class A:
    def d(self):
        return "Function inside A"

class B:
    def d(self):
        return "Function inside B"


class C:
    def d(self):
        return "Function inside C"


class D(A, B):
    def d(self):
        return "Function inside D"


class E(B, C):
    def d(self):
        return "Function inside E"


class F(E,D,C):
    pass

f = F()
print(f.d())
#output: Function inside E
print(F.mro())
#output:[<class '__main__.F'>, <class '__main__.E'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, 
# <class '__main__.C'>, <class 'object'>]