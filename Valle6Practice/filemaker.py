#Created by Felo Malachi Valle

#Input friends name
#Input friends age
#Loop unless user presses enter
#Write to a new file, each on a new line

def main():
    a=0 #Loop Control
    txt=open('friends.txt','w')
    while(a!=1):
        friendsName=str(input('Enter first name of friend or Enter to quit: ')) #Friend Name Input
        #This section closes the file and prints if the response is the ENTER key
        if(friendsName==''):
            txt.close()
            print('File was created')
            a=1 #loop break
        #This section runs if there is any response besides ENTER key
        else: 
            friendsAge=int(input('Enter age (integer) of this friend: ')) #Friends Age Input
            txt.write(f'{friendsName}\n') #writes friends name to File
            txt.write(f'{str(friendsAge)}\n') #writes friends age to File
main()