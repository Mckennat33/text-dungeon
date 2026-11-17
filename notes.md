# Problem Solving 

the exits and you see print statements need to be dynamic for each cell

Remove the continue: line 94 
Updated elif action in room_exits: line 95
1. line 85: needs to be an functionality for player to leave
2. line 81: "options" for an action 
3. line 84: "exit" options for an action - what happens next? 

Where do I put gate is locked? 

# need to check if the door is locked first? 


get_command():
    # show prompt
    # read the input 
    # clean it
    # return it

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
#  (dark: torch                             (locked: needs iron )                                   lever_pulled: True/False
#   )                                   has: lever
#  has: iron key      |
#                   south
#                     |
#                  [ Cell ]  ← START
#                  has: torch, rusty spoon
