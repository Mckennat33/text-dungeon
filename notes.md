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
Someone sees you

# Player instructions
moving go (north, east, west, south)
look - describe the room 
take (item)
inventory (see what you are carrying)
use (item)
help - show this list
quit - end game 