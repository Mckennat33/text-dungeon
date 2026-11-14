# print start story of the game - maybe a play or exit option
#  
import sys

# we want to exit the game a user enters exit
    # gameOn is true until he hits exit
# we want to say not a command if its not one of the option. 
# 
gameOn = True
while gameOn: 
    print('You wake on stone cold. The cell door hangs open. Somewhere above, water drips. Find a way out. ')
    start = print('Type Start or Exit: ', end='')
    initGame = input()
    if initGame.lower() in ['start', 'exit']:
        print('INITIAL COMMAND')
    else:
        gameOn = False
        # if this doesnt end the program we need to find a way to end it
print('GAME ENDED')





# press play - starts the game and the story 





# You wake up in an empty cell, the cell door is locked, look for something to open the gate
    # Key you found it, opens the gate and you walk into a corridor heading north 
        # south option (head back in cell exit game)
        # north keep playing
# text You enter a Corridor - each direction puts you in a different room 
    # west, north, east, south 
        # north = another corridor - left or right? = which one is WIN??
        # west [crypt]- dark: needs torch needs has: iron key
        # east [guard room] locked: needs iron key has:lever
        # south [cell] Start Has: torch, rusty spoon 


# COMMANDS
#   go <direction>   move north, south, east, or west (or n/s/e/w)
#   look             describe the room again
#   take <item>      pick something up
#   inventory        see what you're carrying
#   use <item>       use an item (like pulling a lever)
#   help             show this list
#   quit             end the game


#                 [ Gate ]  ← WIN (needs lever pulled)
#                     |
#                   north
#                     |
# [ Crypt ] --west-- [ Corridor ] --east-- [ Guard Room ]
#  (dark: needs                             (locked: needs iron key)
#   torch)                                   has: lever
#  has: iron key      |
#                   south
#                     |
#                  [ Cell ]  ← START
#                  has: torch, rusty spoon