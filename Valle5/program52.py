### program52.py
### LATE
import functions

convertdy=functions.convertdy
convertyd=functions.convertyd

def main():
    a=float(input('Enter the value to convert: '))
    b=str(input('Enter D or Y to convert enterted value to Yuan(s) or Dollar(s): '))
    if (b=='D'):
        print(f'The value {a:.1f} Yuan(s) converts to {convertyd(a):.2f} Dollar(s).')
    elif (b=='Y'):
        print(f'The value {a:.1f} Dollar(s) converts to {convertdy(a):.2f} Yuan(s).')
    else:
        print('INVALID')
main()