# import importlib
# import sample
# importlib.reload(sample)#with the help of reload we can call the print function in sample.py
#                         #multiple times.
# importlib.reload(sample)
import Filechanges
import importlib
def changes():
    importlib.reload(Filechanges)
    try:
       Filechanges.print_changes()#as you add new files, this will reflect all the changes.
    except:
        pass
    
for i in range(5):
    changes()
    input('Hit enter to reload ...')

