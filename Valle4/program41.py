#Created by Felo Malachi Valle

#Set a sentinel value
#Create counter variable in order to calculate average later
#Use a while loop to add any amount of numbers
#Convert the string input to integer only when the string is not the sentinel value

#Initialized variables
sum=0
userInput='0'
counter=0

print('Enter Integers and when done, S to calculate the average')

while userInput!= 'S':
    userInput=input('Integer: ')
    if userInput!='S':
        sum+=int(userInput) #To Integer
        counter+=1

print(f'The average of values entered is {sum/counter:.2f}')