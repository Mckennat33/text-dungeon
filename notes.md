# Problem Solving 

User enters the games
Yes or no

Goes to play function 
	Current room he is in - is it dynamic
	Description of room 
    enter a command / direction
        function command (player instructions)
        what we expect the input to be? =  north, look, torch, quit

PROBLEM - 

get_command - what the player can do. 
rooms - data
        
maybe change while loop at the top and 
-----------------------------------


Look
Take
Inventory
Use 
Help
Quit

WIN: escape through the gate
 └─ needs: gate opened
     └─ needs: pull the lever (in the Guard Room)
         └─ Guard Room is locked → needs: iron key
             └─ key is in the Crypt
                 └─ Crypt is too dark to enter → needs: torch
                     └─ torch is in your starting Cell

What does the player need to do to win. 

DESIGN THE GAME

# Items 
torch 
key 
lever
*item that does nothing
# Rooms
Cell 
Crypt 
Closet 
Chest
Guard Room 

# Found it Wins (door opens, chest unlocked)

# Loses 
Trap Door 

# Player instructions
moving go (north, east, west, south)
look - describe the room 
take (item)
inventory (see what you are carrying)
use (item)
help - show this list
quit - end game 


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
