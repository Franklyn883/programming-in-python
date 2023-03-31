# #python uses Object oriented programming as a paradigm. OOP relays heavily on simplicity 
# #and reusability to improve workflow # paradigm simply means style of writing codes.
# #OOP relays on components such as: class, objects and methods to achieve it aims.


#---------------------------CLASS-----------------------------------------
#declaring a class
class MyClass:
    #pass #this is to tell python that this is an empty class, but we will do something
          #with it later, else it throws an error.
   # print('hello world')
   a = 5
   def sayHello(self):#inorder for the child class to be able to access this method reference
                      #we need to pass a self argument to the method. You can use any other word. But self is 
                       # just a convention. self points to the instance of the class
      return "Hello i am a method of MyClass"
myclass = MyClass()# this is to instantiate an object of the MyClass. So this is a child
                  # and has access to the attributes(variables) and behavior reference of
                  #the class
print(myclass.a)#myclass has access to the attribute reference of the a variable.
#output: 5
print(myclass.sayHello())#the subclass myclass can also access the method
#output Hello i am a method of MyClass

#Examples
# class House:
#    '''
#    This is a stub for a class representing a house that can be used to create an object and
#    evaluate different metrics the we may require in constructing it.
#    '''
#    num_rooms = 5
#    bathrooms = 2
#    def cost_evaluation(self,rate):#we can pass in any number of arguments, but first one is 
#                                   #always a reference to the instance of the class
                                
#       cost = rate *self.num_rooms
      
#       return cost
#    #functionality to calculate the costs from the area of the house.
# #we can call this class directly or instantiate an object of the class
# house = House()
# print(house.bathrooms)
# print(House.bathrooms)
# #now lets update the value of the child class
# house.bathrooms = 7
# print(house.bathrooms)#this changes
# print(House.bathrooms)#but this still remains the same.
# House.bathrooms = 5#change of the parent attribute no longer affect the obj.
# print(house.bathrooms)
# print(House.bathrooms)
# House.num_rooms = 7#This affects it because the object does not have it's own defined num_room
# print(house.num_rooms)
# #now let call the method
# print(house.cost_evaluation(100))

# #----------------INSTANTIATE A CUSTOM OBJECT------------------
# #Code reusability is a big part of OOP, being able to write a piece of code and reuse it at different instance to
# #generate different results is the flex of OOP. OOP can create custom Object using Two methods.

# # class Recipe():
# #    '''
# #    There are two method of creating a custom object
# #    '''
# #    #new method
# #    def __new__(cls) -> Self:
# #       pass
# #    #the init method takes obj created with new method along with other arguments to instantiate the new 
#       object being created
# #    def __init__(self) -> None:#the self keyword stand as the self reference to the new object created. 
#                                  Just like "this" keyword in js
# #                               

# #Example
# class Recipe():
#    def __init__(self,dish,items,time) -> None:#Here is a template of our new object
#       self.dish = dish
#       self.items = items
#       self.time = time

#   #lets create a method that will read out the string and tells us how long it will take to prepare a dish
#    def contents(self):
#       print('The ' + self.dish + " has " + str(self.items) + " and takes " + str(self.time)+ \
#             " minutes to prepare")

# #We can create instances of this object
# pizza = Recipe('Pizza', ["cheese","bread", "tomatoes"], 45)
# pasta = Recipe('Pasta', ["penne", "sauce"], 30)
# egg_sauce = Recipe('Egg Sauce', ['eggs', "tomatoes", "pepper", "onions"], 15)
# print(pizza.items)
# #output: ['cheese', 'bread', 'tomatoes']
# print(pasta.items)
# #output:['penne', 'sauce']
# print(egg_sauce.items)
# #output: ['eggs', 'tomatoes', 'pepper', 'onions']
# pizza.contents()
# #output: The Pizza has ['cheese', 'bread', 'tomatoes'] and takes 45 minutes to prepare
# pasta.contents()
# #output: The Pasta has ['penne', 'sauce'] and takes 30 minutes to prepare
# egg_sauce.contents()
# #output: The Egg Sauce has ['eggs', 'tomatoes', 'pepper', 'onions'] and takes 15 minutes to prepare

# class MyFirstClass():
#     print("Who wrote this?")
#     index = "Author-Book"

#     def hand_list(self, philosopher, book):
#         print(MyFirstClass.index)
#         print(philosopher + " wrote the book: " + book)

# whodunnit = MyFirstClass()
# whodunnit.hand_list("Sun Tzu", "The Art of War")

# #--------------------INSTANCE METHODS--------------
# #This class creates an instance that can be used to check if an employee has being paid or not.
# class Pays_slip:
#     def __init__(self,name,payment,amount) -> None:
#         self.name = name
#         self.payment = payment
#         self.amount = amount
# #the method updates the payment status
#     def pay(self):
#         self.payment = "yes"
        
#     def status(self):
#         if self.payment == "yes":
#             return self.name + " is paid " + str(self.amount)
#         else:
#             return self.name + " is not paid yet"

# #lets instantiate an object off the class
# nathan = Pays_slip('Nathan', "no" , 1000)
# print(nathan.status())
# nathan.pay()#
# print("After")
# print(nathan.status())
# jonas = Pays_slip("Jonas", "no", 500)
# print(jonas.status())

#-------------------Parent class vs Child Classes------------------------------------
#super class
class Employees:
    def __init__(self, name,last) -> None:
        self.name = name
        self.last = last

#This is inheritance in practice.
#subclass
class Supervisors(Employees):#It inherit all the 
    def __init__(self, name, last, password) -> None:#added property
        super().__init__(name, last)#the inherited property
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return self.name +" " + self.last + " Requesting for " + str(days) + "days of leave"
    
adrian = Employees("Adrian", "K")
emily = Supervisors('Emily',"J","apple")
jerry = Chefs("Jerry",".K" )
#print(jerry.last)
print(jerry.leave_request(10))
#output: Jerry .K Requesting for 10days of leave


