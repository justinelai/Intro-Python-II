class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self, item): 
        return f"You have picked up {item.name}"

    def on_drop(self, item):
        return f"You have dropped {item.name}"