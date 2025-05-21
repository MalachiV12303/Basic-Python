#Created by Felo Malachi Valle

#Use a for in range loop to display multiples of 3 between 3 and 33
#Use a while loop in order to display multiples of 4 between 4 and 48

print('The output below is using the python for loop!')
for value in range(3, 34, 3):
    print(f'{value}', end=' ') #Used end in order to add onto the same line
    
print('') #Redundant, but the module check expected and empty string between the two print statements

print('\nThe output below is using the python while loop!')
value2=4
while (value2<= 48):
    print(f'{value2}', end=' ')
    value2+=4 #Adds 4 AFTER the value has been printed.