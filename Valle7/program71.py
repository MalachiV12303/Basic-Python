#Created by Felo Malachi Valle
#Write a program that can manipulate random integers, and be able to manipulate lists

import random

def main():
    nums=[] #Empty List
    #Adds 19 random integers
    for x in range(0,19):
        nums.append(random.randint(11, 99))
    #Prints these integers on the same line
    for a in nums:
        print(f'{a}', end=' ')
    #Sum the list, then print the sum value.
    total=0
    for a in nums:
        total+=a
    print(f'\nSum of the Random numbers list is {total}')
    #Sort the list
    nums.sort()
    #Print sorted values using unpack feature
    print(*nums)
    #Start list creation
    start=nums[0:5]
    print(start)
    #Finish list creation
    finish=nums[14:19]
    print(finish)
    #Even odd function
    e,f=even_odd(nums)
    #Prints sum of evens and odds, as well as closing message
    print(f'The sum of Even\'s is {e} The Sum of Odd\'s is {f}')
    print('This completes the Last program of COP1000 #1469 :)')

    
def even_odd(a):
    c=0 #Number of Evens
    d=0 #Number of Odds
    e=0 #Sum of Evens
    f=0 #Sum of Odds
    for b in a:
        if(b%2)==0:
            c+=1 #Add 1 to amount of evens
            e+=b #Adds current even to the even total
        else:
            d+=1 #Add 1 to amount of odds
            f+=b #Adds current odd to the odd total
            
    print(f'List had {c} evens and {d} odds')
    print(f'The 13th element in sorted nums is {a[12]}') #Prints the 13th number
    
    return e,f #Returns the sum of evens and odds
main()