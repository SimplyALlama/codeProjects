import random as rn

rn.seed(10)

player = 0
comp = 0

pWin = False
draw = False

again = True

rock = 1
scissors = 2
paper = 3

while (again == True):
    print()

    print('Rock, Paper or Scissors?')
    pIn = input()

    if (pIn == 'Rock' or  pIn == 'rock' or  pIn == 'r' or  pIn == 'R'):
        player = rock
        print ('player: rock')

    elif (pIn == 'Paper' or pIn == 'paper' or pIn == 'p' or pIn == 'P'):
        player = paper
        print('player: paper')

    else:
        player = scissors
        print('player: scissors')


    cThrow = rn.randint(1, 3)

    if (cThrow == 1):
        comp = rock
        print('computer: rock')

    elif (cThrow == 2):
        comp = scissors
        print('computer: scissors')

    else:
        comp = paper
        print('computer: paper')


    if (player == 1 and comp == 2):
        pWin = True

    elif (player == 2 and comp == 3):
        pWin = True

    elif (player == 3 and comp == 1):
        pWin = True

    elif (player == comp):
        draw = True

    else:
        pWin = False

    if (pWin == True and draw == False):
        print('Player wins')

    elif(pWin == False and draw == False):
        print('Computer wins')

    elif (draw == True):
        print('Draw')


    print('play again?')
    aIn = input()

    if (aIn == 'Yes' or aIn == 'yes' or aIn == 'y' or aIn == 'Y'):
        again = True
    
    else:
        again = False