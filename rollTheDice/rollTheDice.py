import random as rn

rn.seed(10)

again = True

while (again):
    total = 0
    i = 0
    print('How many sides your dice have?')
    sides = int(input())

    print('How many dice would you like to roll?')
    rollNum = int(input())

    print()

    while i < (rollNum):
        roll = rn.randint(1, sides)
        print(roll)
        total += roll
        i += 1

    print('The total of your rolls is', total)

    print('would you like to roll again?')
    aIn = input()

    if (aIn == 'Yes' or aIn == 'yes' or aIn == 'y' or aIn == 'Y'):
        again = True
        
    else:
        again = False

    print()