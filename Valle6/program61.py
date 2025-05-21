#Created by Felo Malachi Valle

###Main Method###
def main():
    create()
    retrieve()

###Create Method###
#PSEUDOCODE
    #Create a new file named grades.txt and open it in the program
    #Prompt user for course name followed by percent grade
    #Add course name and GPA value to grades.txt on new lines
    #Once user is complete, they will press ENTER to break a loop
    #Once loop is broken, close the file and print complete statement
def create():
    
    a=0 #Loop Control
    d=0 #GPA Number
    
    txt=open('grades.txt', 'w') #'w' modifier overwrites existing file and creates one if one does not exist
    while(a!=1):
        b=str(input('Enter course name or Enter to quit: ')) #Course Name Input
        #This section closes the file and prints if the response is the ENTER key
        if(b==''):
            txt.close()
            print('File was created and closed')
            print('')
            a=1 #loop break
        #This section runs if there is any response besides ENTER key
        else: 
            c=int(input('Enter grade (integer) achieved: ')) #Percentage Grade Input
            #This section converts the percentage to a GPA value between 0-4, and assigns it to (d) variable
            if(c>89):
                d=4
            elif(c>79):
                d=3
            elif(c>69):
                d=2
            elif(c>59):
                d=1
            else:
                d=0
            txt.write(f'{b}\n') #writes Course Name (b) to File
            txt.write(f'{str(d)}\n') #writes GPA Number (d) to File
    return 1 #returns boolean true

###Retrieve Method###
#PSEUDOCODE
    #Open the grades.txt file
    #Collect the first and second lines of code
    #If the lines are not empty, print statement with given data
    #Repeat until lines are empty
    #Once empty, print the average GPA
def retrieve():

    a=0 #Loop Control
    d=0 #Total GPA Number
    e=0 #Divisor for average calculation
    
    txt=open('grades.txt','r') # r modifier is read only
    print('Here is your GPA for the classes you entered:')
    while(a!=1):
        b=txt.readline() #collects the first line, the Course Name
        c=txt.readline() #collects the second line, the GPA Number
        #This section runs if the lines that were read are not empty, this accounts for as many entries possible
        if (b!=''and c!=''): 
            b=b.rstrip('\n')
            c=c.rstrip('\n')
            print(f'{b} class GPA {c}') #prints lines after removing the \n from the string
            d+=int(c) #converts the GPA Number (c) to an integer and adds it to Total GPA Number (d)
            e+=1 #adds 1 to the divisor for each iteration
        #This section runs if the read lines were empty, signaling the end of the data
        else: 
            print(f'Your GPA for all classes entered is {d/e:.2f}')
            a=1 #loop break
    return d/e #returns average

#Main call, the auto run was not working and I don't fully understand how the test program works
main()