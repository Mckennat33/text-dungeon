
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
# commands = ['go', 'look', 'use: <item>', 'take: <item>', 'inventory' ,'help', 'quit']
commands = {
    'go': 'north, south, east, west', 
    'look': 'Describe the room', 
    'use': '<item>',
    'take': '<item>', 
    'inventory': '<items in inventory>',
    'help': 'this list',
    'quit': 'Exit Game', 
}

def show_inventory():
    print(inventory) # need to add functionality

def handle_command(prompt, current_room):
    # 'look', 'use', 'take', 'inventory' ,'help', 'quit'
    if prompt == 'quit':
        exit_game()

    if prompt == 'go'.join(''):
        print(prompt)

    elif prompt == 'look':
        if current_room in rooms: 
            print(rooms[current_room]['description'])

    elif prompt == 'use':
        use_item(current_room)

    elif prompt == 'take':
        take_item(current_room)

    elif prompt == 'inventory':
        if inventory == []: 
            print("You don't have anything in your inventory")
        else:
            for items in inventory:
                print(items)

    elif prompt == 'help':
        for key, value in commands.items():
	        print(f"{key}: {value}")


def use_item(current_room):
    # input - use 
    # output - 
    # statagy. 
    if inventory == []:
        print('You have no items in your inventory')
    else: 
        print('You used a item we, need to add functionality')
    

def take_item(current_room):
    print('take item action used')

    
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
        go_action = action.split()
        if action in commands: 
            handle_command(action, current_room) 
        elif len(go_action) == 2 and go_action[0] == 'go' and go_action[1] in room_exits: 
            if locked == True:
                print(lockedM)
            else:
                player_action(action, current_room)
        else:
            print('that is not a command')


start_game()
play()