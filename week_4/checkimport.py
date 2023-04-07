import modules # this will import all the codes from module.py
#to import a python file from a different directory we use:
import sys
sys.path.insert(1,r'/home/frank/repos/programming-in-python/week_3')
import sample
print(sample.a)