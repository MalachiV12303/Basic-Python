#Created by Felo Malachi Valle

#Read the first and second lines
#Print the response
#Loop until lines are empty
#Then print the average age using a accumulator and counter

def main():
    a=0 #Loop Control
    totalAge=0 #Total Friends Age
    numOfFriends=0 #Divisor for average calculation
    txt=open('friends.txt','r') # r modifier is read only
    while(a!=1):
        friendName=txt.readline() #collects the first line
        friendAge=txt.readline() #collects the second line
        #This section runs if the lines that were read are not empty, this accounts for as many entries possible
        if (friendName!=''and friendAge!=''): 
            friendName=friendName.rstrip('\n')
            friendAge=friendAge.rstrip('\n')
            print(f'My friend {friendName} is {friendAge}') #prints lines after removing the \n from the string
            totalAge+=int(friendAge) #converts the Friend Age to an integer and adds it to Total Friend Age
            numOfFriends+=1 #adds 1 to the divisor for each iteration
        #This section runs if the read lines were empty, signaling the end of the data
        else: 
            print(f'Average age of friends is {totalAge/numOfFriends:.1f}')
            a=1 #loop break
main()