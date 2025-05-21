#Created by Felo Malachi Valle

#Input the selling price of the house
#Input the commission rate.
#Assign new variable the product of the price of the house and the commission rate.
#Display result

#Accepts user input of price
price = float(input('Please enter the selling price of the house: '))
#Accepts user input and converts it to a decimal for future calculations.
commission = (float(input('Please enter the commission rate as a percentage: ')))/100
#Calculates commission
earnedCommission = price*commission
#Displays results
print(f'Your commission earned on the sale of this home would be ${earnedCommission:,.2f}')