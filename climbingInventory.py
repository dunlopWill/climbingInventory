# climbingInventory.py

# The function displayInventory() takes a dictionary of 'inventory'.
# The function prints a list of the inventory in the format "number of items x item".
# The function also logs the total number of items of inventory and prints this total.

# The function addToInventory() takes a list of items and adds these items to the dictionary.
# If the item key is already in the dictionary, it updates the number.
# If the item key is not already in the dictionary, it adds the item to the dictionary.

# The function removeFromInventory() takes a lsit of items and removes these from the dictionary and updates the number accordingly.

# Dictionary of climbing inventory
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

#Function to display dictionary
def displayInventory(inventory):
    print("Climbing inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(k + " x " + str(v))
        item_total+=v
    print("Total number of items: " + str(item_total))

#Function to add list items to dictionary
def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] in inventory:
            inventory[addedItems[i]] += 1
        else:
            inventory[addedItems[i]] = 1

#Function to remove list items from dictionary
def removeFromInventory(inventory, lostItems):
    for i in range(len(lostItems)):
        if lostItems[i] in inventory:
            inventory[lostItems[i]] -= 1

shop = ['Screwgate carabiners', 'Nylon slings', 'Cord', 'Cord']
lost = ['Hexes', 'Hexes', 'Hexes']

#Testing/running of programme
displayInventory(climbingInventory)

addToInventory(climbingInventory, shop)
displayInventory(climbingInventory)

removeFromInventory(climbingInventory, lost)
displayInventory(climbingInventory)