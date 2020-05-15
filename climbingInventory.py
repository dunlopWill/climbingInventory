# climbingInventory.py
# The function displayInventory() takes a dictionary of 'inventory'.
# The function prints a list of the inventory in the format "number of items x item".
# The function also logs the total number of items of inventory and prints this total.

climbingInventory = {
'Helmet': 1,
'70 meter rope': 1,
'40 meter rope': 6,
'Harness': 1,
'ATC belay device': 1,
'Quickdraws': 12,
'Screwgate carabiners': 8,
'Snapgate carabiners': 14,
'Nylon slings': 3,
'Dyneema slings': 4,
'Prussiks': 4,
'Cams': 6,
'Hexes':3
}

def displayInventory(inventory):
    print("Climbing inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k + " x " + str(v))
        item_total+=v
    print("Total number of items: " + str(item_total))

displayInventory(climbingInventory)