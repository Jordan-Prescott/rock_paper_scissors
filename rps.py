#Game of Rock, Paper, Scissors

#Imports
import random, sys

#Source Code

print('ROCK, PAPER, SCISSORS')

#Variables
wins = 0
loss = 0 
draws = 0 

# MAIN GAME 
# ----------------------------------------------------------- #
while True: 
    print('%s Wins, %s Losses, %s Draws' % (wins, loss, draws))
    while True: # Player input
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            print('Thanks for playing!')
            sys.exit() # Quit program
        if playerMove == 'r'or playerMove == 'p' or playerMove == 's':
            break # Break out of the player input loop.
        print()
        print(
            '''Thats not a valid option, are you dumb? 
Win or lose now you lose for that.'''
        )
        print('Type one of r, p, s, or q.')

    # Display Player Choice
    # --------------------------------------------------------#
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus...')

    # Display Computer Choice
    # --------------------------------------------------------#
    RandomNumber = random.randint(1,3)
    if RandomNumber == 1:
        ComputerMove = 'r'
        print('ROCK')
    elif RandomNumber == 2:
        ComputerMove = 'p'
        print('PAPER')
    elif RandomNumber == 3:
        ComputerMove = 's'
        print('SCISSORS')
    
    # Display & Record win/loss/draw
    # --------------------------------------------------------#
    if playerMove == ComputerMove:
        print('Its a draw')
        draws = draws + 1 
    
    elif playerMove == 'r' and ComputerMove == 's':
        print('You Win!')
        wins = wins + 1
    
    elif playerMove == 'p' and ComputerMove == 'r':
        print('You Win!')
        wins = wins + 1
    
    elif playerMove == 's' and ComputerMove == 'p':
        print('You Win!')
        wins = wins + 1
    
    elif playerMove == 'r' and ComputerMove == 'p':
        print('You Lose!')
        loss = loss + 1
    
    elif playerMove == 'p' and ComputerMove == 's':
        print('You Lose!')
        loss = loss + 1
    
    elif playerMove == 's' and ComputerMove == 'r':
        print('You Lose!')
        loss = loss + 1 
