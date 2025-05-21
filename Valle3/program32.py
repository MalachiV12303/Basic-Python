#Created by Felo Malachi Valle

#Define constant prices
#Input shirts
#Calculate discounts and shipping fees
#Display results

#Constants
shirtPrice=11.99
shippingFee=1.05
#Constant used for boolean check later
isValid=1

#Shirt input
shirts=int(input('Enter how many Tee\'s shirts would you like to order today?'))

#if elif statements that determine total shirt priced with discounts
if (shirts>=10):
    totalShirtPrice=(shirts*shirtPrice)-((shirts*shirtPrice)*0.3)
elif (shirts>=6):
    totalShirtPrice=(shirts*shirtPrice)-((shirts*shirtPrice)*0.2)
elif (shirts>=3):
    totalShirtPrice=(shirts*shirtPrice)-((shirts*shirtPrice)*0.1)
elif (shirts>0):
    totalShirtPrice=shirts*shirtPrice
else:
    #Prints invalid if input is invalid and switches boolean check to false
    print('INVALID')
    isValid=0
    
#Calculates totalshippingfee after previous elif statement because if INVALID an error is thrown
totalShippingFee=shippingFee*shirts

#Checks to see if boolean is still true
if (bool(isValid)):
    if (shirts>=10): #if statement for use when there is no shipping charge, ONLY because the print() text must be different
        total=totalShirtPrice
        print(f'The Tee Shirts amount is ${totalShirtPrice:,.2f}')
        print('Shipping is FREE on orders of 10 or more Tee Shirts!')
        print(f'Total amount due ${total:,.2f}')
    else: #else statement is triggered if shirts is less than 10, but more than 0
        total=totalShippingFee+totalShirtPrice
        print(f'The Tee Shirts amount is ${totalShirtPrice:,.2f}')
        print(f'Shipping fee added to this order is ${totalShippingFee:,.2f}')
        print(f'Total amount due ${total:,.2f}')