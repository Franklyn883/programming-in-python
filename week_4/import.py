'''
--------------    WRITING IMPORT STATEMENTS----------------------
'''
#We can import modules by using: import [module name] e.g
import math           #this import the math modules and all of it methods
root = math.sqrt(9) #we call the square root method
print(root)#output: 3.0
#This will import the entire math module and it functions, this can overload the interpreter.
#instead we can just import only the sqrt method
from math import sqrt
root = sqrt(16)
print(root)#output 4.0

#Alias: We can decide to rename the module, this reduces your typing effort
import math as m
cosine = m.cos(0)
print(cosine)#output: 1.0

#You can also change the name of  a module method
from math import factorial as f
factorial_10 = f(10)
print(factorial_10)#output:3628800

#you can import multiple method 
from math import factorial, log10, sqrt
x = log10(50)
print(round(x,4))#output: 1.699