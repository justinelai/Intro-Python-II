# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.holdings = []

    def get_items(self):
        myString = []
        for treasure in self.holdings:
            myString.append(str(treasure.name))
        return ', '.join(myString)

    def add_item(self, item):
        self.holdings.append(item)

    def remove_item(self, item):
        if item in self.holdings:
            self.holdings.remove(item)
            return True
        else: 
            print("But the room doesn't have this item!") 
