#CLASSS CREATION
class Item:
    def __init__(self, id, name, description, quantity):
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity
    def display_item_info(self):
        item_display_string = "{self.id} - {self.name}, {self.description} ({self.quantity}))"
        return item_display_string

class Inventory:
    def __init__(self, items):
        self.items = []

#IMPLEMENT THE READ METHOD( read_item() )
    def read_item(self, id):
     item_index += -1
     for items in self.items:
         if item.id == id :
            item_index = self.items.index(item)
            return item_index
#IMPLEMENT THE CREATE METHOD
    def create_item(self, id, name, description, quantity):
        item_index = inventory.read_item(id)
        if item_index == -1 :
            item = Item(id, name, description, quantity)
            self.items.append(item)
            print(item.display_item_info() + "added to inventory...")
        else:
            print("Cannot create an item with a duplicate id")
            print(f"Item: {self.items[item.index].display_item_info()} has the same ID!")
            print("Please change the ID and try adding the item again.")
#IMPLEMENT THE UPDATE METHOD
    def update_method(self, id, new_name, new_description, new_quantity):
        item_index = inventory.read_item(id)
        if item_index != 1:
            print(f"Item updating from : {self.items[item_index].display_item_info()}")
            self.items[item_index].name = new_name
            self.items[item_index].description = new_description
            self.items[item_index].quantity = new_quantity
            print(f"Item updated to : {self.items[item_index].display_item_info()}")
        else:
            print("Cannot update an item that does not exist, try adding an item instead")

#IMPLEMENT A DELETE METHOD
    def delete_method(self, id):
        item_index = inventory.read_item(id)
        if item_index != -1:
            self.items[item_index].pop()



