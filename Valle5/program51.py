### program52.py
### LATE
import random

def main():
    amount=11
    t,a=rnumbers(amount)
    print(rnumbers(11))
    
def rnumbers(arg):
    total=0
    for x in range(arg):
        x=random.randint(12, 73)
        total+=x
        print (f'{x}', end=' ')
    average=total/arg
    return total, average

main()