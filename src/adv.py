from room import Room
from player import Player

# Declare all the rooms

room = {
    "outside": Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    "foyer": Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""",
    ),
    "overlook": Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
    ),
    "narrow": Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
    ),
    "treasure": Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
    ),
}


# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]

#
# Main
#

# Makes a new player object that is currently in the 'outside' room.
val = input("Please enter your name: ")
player = Player(val, room["outside"])

# function to print current status
def print_current(room):
    print(f"You are standing in {room.name}.")
    print(f"...{room.description}")

print_current(player.current_room)
gameover = False

# if (use current_room name) has a x_to is not None
# change value of player.current_room to room value of rooms.x_to  player.current_room = room

while gameover == False:
    move = input("Enter a direction as n/s/e/w. (q to quit) ").lower()
    if move == 'n':
        if player.current_room.n_to:
            player.current_room = player.current_room.n_to
            print_current(player.current_room)
        else:
            print("That move is not permitted. Please try again.")
            gameover = False
    elif move == 's':
        if player.current_room.s_to:
            player.current_room = player.current_room.s_to
            print_current(player.current_room)
        else:
            print("That move is not permitted. Please try again.")
            gameover = False
    elif move == 'e':
        if player.current_room.e_to:
            player.current_room = player.current_room.e_to
            print_current(player.current_room)
        else:
            print("That move is not permitted. Please try again.")
            gameover = False
    elif move == 'w':
        if player.current_room.w_to:
            player.current_room = player.current_room.w_to
            print_current(player.current_room)
        else:
            print("That move is not permitted. Please try again.")
            gameover = False
    elif move == 'q':
        gameover = True
    else: 
        print("Invalid input. Please try again.")
        gameover = False
        
# End game
print("The game has ended.")