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

httpStatus = 200
if httpStatus == 200 or httpStatus == 201:
    print('Success')
elif httpStatus == 400:
    print('Bad request')
elif