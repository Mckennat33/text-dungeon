
import sys

rooms = {
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

inventory = []  
def show_inventory():
    print(inventory) # need to add functionality

def get_command(prompt): 
    # show prompt
    # read the input 
    # clean it
    # return it
    print(prompt)

def exit_game():
    print('You exited the game')
    sys.exit()


def start_game():
    print('You wake on stone cold. Somewhere above, water drips. You need to get out!!')

    while True: # Program runs until while loop is exited:below
        print('Type Start or Exit: ', end='')
        initGame = input('').strip().lower()
        print('================================')
        if initGame == 'exit':
            exit_game()
        elif initGame == 'start':
            break
        else: 
            print('That is not a command')
            

def play(): 
    #what dictates what cell we are in?
    current_rooms = "cell" 
    print("Type 'help' for a list of commands")

    cell_descipription = rooms.get("cell", {}).get("description", {})

    print(cell_descipription)
    print('You see: torch')    
    print('Exits: north')
    while current_rooms == 'cell': # changes the room 
        firstChoice = input('').strip().lower()
        if firstChoice not in ('north', 'look', 'grab torch', 'use', 'help', 'quit'):
            print('not a valid command, press help if needed')
            continue 
        else:
            get_command(firstChoice)

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