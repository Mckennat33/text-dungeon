
import sys

rooms = {# Environment and how they connect
    'cell' : {
        'exits': {'north': 'corridor'}, 
        'description': "It's nearly pitch black. The only light comes from the torch flickering in a bracket on the wall", 
        'items': ['torch', 'rusty spoon'],
        'locked_exits': True,
        'locked_message': "The cell door won't budge but the hinges look loose"
    },
    'corridor' : {
        'exits': {'north': 'gate', 'west': 'storage', 'east': 'guard room', 'south': 'cell'}, 
        'description': '',
        'items': [],
    },
    'storage' : {
        'exits': {'east': 'corridor'}, 
        'description': '',
        'items': ['iron key'],
    },
    'guard room' : {
        'exits': {'west': 'corridor'}, 
        'description': '',
        'items': [],
        "lever_pulled": False,
        "locked": True,
    },
    'gate' : {
        'exits': {'west': 'trap room', 'east': 'win', 'south': 'corridor'}, 
        'description': '',
        'items': [],
    },
    'trap room' : {
        'exits': {}, 
        'description': '',
        'items': [],
    },
    'win' : {
        'exits': {}, 
        'description': '',
        'items': [],
    },

}

inventory = [] # items 
def show_inventory():
    print(inventory) # need to add functionality

def get_command(prompt): # what your player can do 
    print("Get Command")
    # question goes in the prompt text you pass goes to get_command

    # Shows prompt and waits for input. 
    # cleans the answer
    # handles exits everywhere
    # where do I call it? probably in any function that needs a command

def exit_game():
    print('You exited the game')
    sys.exit()


def start_game():
    print('You wake on stone cold. Somewhere above, water drips. You need to get out!!')

    while True: # Program runs until while loop is exited:below
        print('Type Start or Exit: ', end='')
        initGame = input('').strip().lower()
        if initGame == 'exit':
            exit_game()
        elif initGame == 'start':
            break
        else: 
            print('That is not a command')
            

def play(): # practice problem solving
    current_rooms = "cell" 
    print("Type 'help' for a list of commands")

    # cell_descipription = rooms.get("cell", {}).get("description", {})
    # print(cell_descipription)
    # if current_rooms == "cell":
    #     print("You See: torch")
    #     print('Exits')
    


    # pick description of cell
    # User given choices on what he can o 



    # users choice in a variable thats sent to get_command
    # need room description 
    # Options for player and next objective
    # send his answer to get_command
        # write that function


    # get_command - logic
    # rooms information
    
    # for items in cellStartOptions:
    #     print(items)
    # while True:
    #     cellChoice = int(input().strip())
    #     if cellChoice in range(1, 5):
    #         print()      
    #     else:
    #         print('This is not a command')

start_game()
play()







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

                    #adding a top room 
#west (TRAP ROOM)   <- [ Gate ]  ←> WIN (needs lever pulled)
#                     |
#                   north
#                     |
# [ Crypt ] --west-- [ Corridor ] --east-- [ Guard Room ]
#  (dark: needs                             (locked: needs iron key)                                   lever_pulled: True/False
#   torch)                                   has: lever
#  has: iron key      |
#                   south
#                     |
#                  [ Cell ]  ← START
#                  has: torch, rusty spoon

# rooms = {
#     'cell': {
#         'exits': {'north': 'corridor'},
#     },
#     'corridor': {
#         'exits': {'north': 'gate', 'west': 'crypt', 'east': 'guard room', 'south': 'cell'},
#     },
# }