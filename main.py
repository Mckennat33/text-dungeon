
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

    while True: 
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
    current_rooms = "" 
    print("Type 'help' for a list of commands")
    
    cell_descipription = rooms[f"{current_rooms}"]["description"]

    # how do we tell the game what cell to start in 
    print(cell_descipription)
    print('You see: torch')    
    print('Exits: north')
    while True: # makes cell dynamic 
        firstChoice = input('').strip().lower()
        if firstChoice not in ('north', 'look', 'grab torch', 'use', 'help', 'quit'):
            print('not a valid command, press help if needed')
            continue 
        else:
            get_command(firstChoice)

start_game()
play()