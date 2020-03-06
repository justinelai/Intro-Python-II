import sys 
from room import Room
from player import Player
from item import Item

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

# Create items
items={
    "trinket": Item("Trinket", "Looks pretty."),
    "spoon": Item("Spoon", "Allows you to drink soup"),
    "pen": Item("Pen", "Writing tool. If only you had some paper...")
}

# Seed items
room["outside"].holdings.append(items["spoon"])
room["outside"].holdings.append(items["spoon"])
room["outside"].holdings.append(items["pen"])


#
# Main
#

# Makes a new player object that is currently in the 'outside' room.
val = input("Please enter your name: ")
player = Player(val, room["outside"])
print(f"Greetings, {val}. Shall we play a game?")

# function to print current status
def print_current(room):
    print(f"\nYour location is {room.name}")
    print(f"Items in this room: {room.get_items()}")
    print(f"{room.description}...")

# start game
print_current(player.current_room)
gameover = False

# establish valid moves
valid_moves = ["n", "s", "e", "w"]

while gameover == False:
    # prompt for input
    move = input("Enter a direction as n/s/e/w. (i for inventory, q to quit) ").lower()
    split = move.split(" ",1) #Splits string into 2 item list.
    verb = split[0]
    # checks for 2 word inputs
    if len(split) > 1:
        try:
            noun = split[1]
            #handle drop
            if verb == "drop":
                player.remove_item(items[noun])
                player.current_room.add_item(items[noun])
            #handle get
            elif verb == "take" or verb == "get":
                # my special touch - only allows the user to have one of each item
                if player.check_item(items[noun]) == False:
                    # confirms the item is indeed inside the room
                    if player.current_room.remove_item(items[noun]) == True:
                        # woohoo, actually add that item!
                        player.add_item(items[noun])
            else:
                # this doesn't seem to be reachable because the user will always have a key error...
                # ...and the class methods handle more specific errors 
                print("Invalid input. Please try again.")
        except KeyError: 
            #error for all words that aren't existing
            print("Don't know that one. Please try again.")
    else: 
        # checks to see if 1 word input is a valid move
        if verb in valid_moves:
            move_attr = move+"_to"
            validated = getattr(player.current_room, move_attr, None)
            if validated:
                player.current_room = validated
                print_current(player.current_room)
            else:
                print("That move is not permitted. Please try again.")
        elif verb == 'i':
        # check inventory
            print(f"Your inventory: {player.get_inventory()}")
        elif verb == 'q':
        # quit game
            gameover = True
        else: 
        # note that this would apply to drop/get/take inputted as single words - in case we want to return a more specific error
            print("Invalid input. Please try again.")
# Game ending
print("The game has ended.")