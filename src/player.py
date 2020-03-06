# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def get_inventory(self):
        myString = []
        for thingy in self.inventory:
            myString.append(str(thingy.name))
        return ', '.join(myString)

    def check_item(self, item):
        if item in self.inventory:
            print("You already have this item!")  
        else:
            return False        

    def add_item(self, item):
        self.inventory.append(item)
        print(item.on_take(item))

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(item.on_drop(item))
        else:
            print("Impossible! You don't have this item!")