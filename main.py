
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
commands = ['look', 'use', 'take', 'inventory' ,'help', 'quit']
user_menu = ['look', 'use', 'take', 'inventory' ,'help', 'quit']

def show_inventory():
    print(inventory) # need to add functionality

def handle_command(prompt, room_now):
    # 'look', 'use', 'take', 'inventory' ,'help', 'quit'
    if prompt == 'quit':
        exit_game()
        
    elif prompt == 'look':
        if room_now in rooms: 
            print(rooms[room_now]['description'])

    elif prompt == 'use':
        print('use')
    elif prompt == 'take':
        print('take')
    elif prompt == 'inventory':
        print('inventory')
    elif prompt == 'help':
        for list in commands:
            print(list)
    
    
def player_action(action, room):
    print('You pressed ', action, 'You are currently in ', room)

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
    room_descipription = rooms[current_room]["description"] #description
    locked = rooms[current_room]['locked_exit'] # is exit locked
    lockedM = rooms[current_room]['locked_message'] # locked message
    print(room_descipription) 

    while True:  
        room_exits = rooms[current_room]['exits'] #location of exit
        action = input('> ').strip().lower()

        if action in commands: 
            handle_command(action, current_room) 
        elif action in room_exits: 
            print('exit room statement') 
            if locked == True:
                print(lockedM)
            else:
                player_action(action, current_room)
        else:
            print('that is not a command')

start_game()
play()