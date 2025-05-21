#Created by Felo Malachi Valle

#Input full name
#Input hair color
#Input age as int
#Display information in f-string that will add 1 to the given age

#Collects name
name=input('Please enter your full name: ')
#Collects hair color
hairColor=input('Please enter your hair color: ')
#Collects age as interger
age=int(input('Please enter your age: '))
#Prints results
print(f'My name is {name}, my hair is {hairColor} and on my next birthday I will be {age+1} years old')