##conditional if and else statememt, in python
#billTotal = 220
#discount1 = 10
#discount2 = 20
# 
#if billTotal > 100 and billTotal < 200:
#    print('bill is greater than 100')
#    billTotal = billTotal - discount1
#    print('bill Total is: ' + str(billTotal))
#elif billTotal > 200:
#    print('bill is greater than 200')
#    billTotal = billTotal - discount2
#    print('bill Total is: ' + str(billTotal)) 
#  
#else:
#    print('bill is not upt to 100')
#    print('bill Total is: ' + str(billTotal))
#

#Light is currently off
#current = False
#
#if current:
#    current = False
#    print('Turning light off')
#
#if not current:
#    current = True
#    print('Turning light on') 


# A simple programme to check if a customer is in a loyalty programme. if they are in a loyalty programme and spend
# above 100, a discount of 20% is applied. If they are not in the loyalty programme a service charge of 5% is 
# applied, if they are in the programme but spent less than 100, no charges is deducted.

#loyaltyProgramme = True
#billTotal = 124
#if loyaltyProgramme == True and billTotal > 100:
#    billDiscount = (billTotal * 20)/100
#    billTotal = billTotal - billDiscount
#    print('your total bill is: ' + str(billTotal) + ' and you discount is: ' + str(billDiscount))
#elif loyaltyProgramme == False :
#    serviceCharge = (billTotal * 5) /100
#    billTotal = billTotal + serviceCharge
#    print('Your total bill is: ' + str(billTotal) +' and your service charger is: ' + str(serviceCharge))
#else:
#    print('Your total bill is: ' + str(billTotal) + ' No discount')   

#using the match statement: the match statement is equivalent to javascript switch statement.

#httpStatus = 200
#if httpStatus == 200 or httpStatus == 201:
#    print('Success')
#elif httpStatus == 400:
#    print('Bad request')
#elif httpStatus == 404:
#    print('Not Found')
#elif httpStatus == 500 or httpStatus == 501:
#    print('Server Error')
#else:
#    print('Unknown')    

##Using the match method for the conditional control flow
#match httpStatus:
#    case 200 | 201 :
#        print('Success')
#    case 400:
#        print('Bad request')
#    case 404:
#        print('Not Found')
#    case 500 | 501:
#        print('Server Error')
#    case _:
#        print('Unknown')

## Looping construct the For Loop

#favorites = ['creme brulee', 'Apple pie', 'Churros', "chocolate", 'pancake']
#for i in favorites:
 #   print('i like :', i)

#using the while loop: first we initiate a counter, the provide the condition of the loop, and update the counter
# after each iteraction until the condition is met.
#count = 0
#while count < len(favorites):
#    print('I like this dessert: ', favorites[count]) 
#    count += 1

#Controlling flow with if/else statement in a loop. using break, continue and pass
##favorites = ['creme brulee', 'Apple pie', 'Churros', "chocolate", 'pancake', 15]
##for dessert in favorites:
##    if dessert != str(dessert):
##        print('my favorite dessert is:', dessert)
##        pass
##else:
 #       print('sorry dessert not found')

#Nested Loop a loop wetin a loop
#outer loop
#for i in range(10):
#    for y in range(10):
#        print(0, end=" ")
#    print()    
# Function is defined using def


def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100,2)
print('Your tax is: ', calculate_tax(112.34,15))