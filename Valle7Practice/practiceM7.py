#Created by Felo Malachi Valle

import random
def main():
    myList=[] #Create empty list
    for x in range(0,12): #Adds 12 random numbers to the new list
        myList.append(random.randint(50, 100))
    for x in myList:
        print(f'{x}', end=' ')
    print(f'The 4th element in the list is {myList[3]}') 
    print(f'The element at index 9 is {myList[9]}')
    print(f'The smallest element in the list is {min(myList)}') #min() returns the smallest value in the list
    print(myList)
    newList=changeList(myList) #Calls changeList function
    print('change_list returned this sorted list...')
    #Prints newList
    for x in newList:
        print(f'{x}', end=' ')

#This function slices the list, prints the size, then returns the sorted list
def changeList(a):
    b=a[3:9] #Slices middle six elements
    print(f'The size of the list is now {len(b)}') #Use len() function to return list length
    b.sort() #Use .sort() to sort in ascending order
    return b
    
main()