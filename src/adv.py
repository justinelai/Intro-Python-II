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

# start game
print_current(player.current_room)
gameover = False

# establish valid moves
valid_moves = ["n", "s", "e", "w"]

while gameover == False:
    # prompt for input
    move = input("Enter a direction as n/s/e/w. (q to quit) ").lower()
    # checks to see if move is valid and exists as an attribute.
    if move in valid_moves:
        move_attr = move+"_to"
        validated = getattr(player.current_room, move_attr, None)
        if validated:
            player.current_room = validated
            print_current(player.current_room)
        else:
            print("That move is not permitted. Please try again.")
    elif move == 'q':
        gameover = True
    else: 
        print("Invalid input. Please try again.")
        
# End game
print("The game has ended.")