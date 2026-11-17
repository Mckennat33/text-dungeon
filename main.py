
import sys

rooms = {
    'cell' : {
        'exits': {'north': 'corridor'}, 
        'description': "It's nearly pitch black. The only light comes from the torch flickering in a bracket on the wall, a rotting bed sits in the corner", 
        'items': ['torch', 'rusty spoon'],
        'locked_exit': True,
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

def handle_command(prompt):
    print('================================')
    print(f"You pressed {prompt}")

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
    current_room = "cell" 
    print("Type 'help' for a list of commands")
    room_descipription = rooms[current_room]["description"]
    locked = rooms[current_room]['locked_exit']
    lockedM = rooms[current_room]['locked_message']
    print(room_descipription)
    while True:  
        room_exits = rooms[current_room]['exits'] 
        action = input('').strip().lower()
        if action in ('look', 'use', 'take', 'inventory' ,'help', 'quit'): 
            handle_command(action, current_room) 
        elif locked == True:
            print(lockedM)
        else:
            print('that is not a command')

start_game()
play()