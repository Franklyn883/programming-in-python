'''
---------------------NAMESPACE AND SCOPE-----------------
In Python, a namespace is a mapping from names to objects. It's a way to organize objects and avoid naming collisions.
When you define a variable or function in Python, it's added to the current namespace.
  Scope is the textual region where the namespace is accessible. There are four types of scope in python: Local,
Enclosed, Global and Built-in(LEGB). The practice of finding a variable scope is known as "Scope Resolution".
python uses the LEGB model to try to find the scope of the variable. Using global scope is not a good practice, it can
result to errors and spaghetti codes.
'''
#Example:
greek = "alpha"
print("Global declaration: " +  greek, id(greek))#output:Global declaration: alpha 140358603515440
def b():
    greek = 'beta'
    print("Inside Local: "+ greek,id(greek))#output:Inside Local: beta 140358603515248
    def c():
        greek = "gamma"
        print("Inside Enclosed: " + greek, id(greek))#output:Inside Enclosed: gamma 140358603562672
    c()
b()
'''
There are two keyword to change the scope of a variable: global and nonlocal
global -> helps us access the global variable from within a function
nonlocal ->this is used in a nested function, with the condition that the variable was already defined in the
enclosing function
'''
def d():
    animal = 'elephant'
    def e():
        nonlocal animal #changes the value of the enclosed function
        animal ="giraffe"
        print('Inside nested function ' + animal)#output:Inside nested function giraffe
    print("Before calling function: " + animal)#output:Before calling function: elephant
    e()
    print("After calling function: " + animal)#output:After calling function: giraffe
animal ="camel"
d()
print("Global animal : " + animal)#output:Global animal : camel