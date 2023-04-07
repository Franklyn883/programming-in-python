'''
Modules are building blocks for adding functionality to your code, so you don't need to 
everything every time. It contains statements and definitions. They can be imported.
They can contain executable statements and definitions.
'''
#--------------ACCESSING MODULES
'''
any python file can be a module. Module is searched in by the interpreter in the following
sequence:
current directory -> Built-in modules -> PYTHONPATH -> Installation dependent default direc-
tory
'''
import sys
import calendar
locations = sys.path # This shows all the possible path python interpreter will check to
                     #to  locate the module

for i in locations:
    print(i)

leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
is_it_leap = calendar.isleap(2035)
print(is_it_leap)