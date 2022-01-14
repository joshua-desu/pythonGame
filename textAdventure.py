#Show the rules of the game
def show_instructions():
    print("Summon the Goddess Game\n","Qlippothic forces have broken their way into reality and threaten place the universe in an endless \n"
          "state of peril. You are an adept initiate of a secret magical order and must use your inner knowledge  \n"
          "to seal the demon Choronzon back into the negative abyss. You must recover the ritual weapons, which have  \n"
          "been hidden at various Tokyo train station coinlockers, to summon the sun goddess Amaterasu and restore  \n"
          "harmony. The hooded cloak is waiting at Shibuya Station, the dagger is stored at Ueno Station, the magic  \n"
          "bell is found at Shinjuku Station, the sacred cup is sitting in locker #444 at Ebisu Station, the  \n"
          "magus’s wand is hidden at Asakusa Station, and holy oil can be collected at Meiji Jingu Station. Be ever \n"
          " weary eternal wander! Time is of the essence. If you take the wrong line, you will fall prey to madness  \n"
          "at the hands of Choronzon. Collect 6 Items to summon Amaterasu, or perish before Choronzon. \n", "\nRULES", "\nMove commands: go South, go North, go East, go West\n Add to Inventory: get 'Item name'\n")
show_instructions()

# Define the locations the player can visit
rooms = {
    'Tokyo Station': {'South': 'Ebisu Station', 'North': 'Shinjuku Station', 'East': 'Ueno Station', 'West': 'Shibuya Station', 'Item': 'locker with nothing in it.'},
    'Meiji Jingu Station': {'West': 'Ebisu Station', 'Item': 'Holy Oil'},
    'Ebisu Station': {'North': 'Tokyo Station', 'East': 'Meiji Jingu Station', 'Item': 'Cup'},
    'Akihabara Station': {'South': 'Ueno Station', 'Item': 'Choronzon'},
    'Ueno Station': {'West': 'Tokyo Station', 'North': 'Akihabara Station', 'Item': 'Dagger'},
    'Shinjuku Station': {'East': 'Asakusa Station', 'Item': 'Bell'},
    'Shibuya Station': {'East': 'Tokyo Station', 'Item': 'Cloak'},
    'Asakusa Station': {'West': 'Shinjuku Station', 'Item': 'Wand'},
               }

# Define variables
currentRoom = 'Tokyo Station'
inventory=[]


# Code to control movement
def get_new_currentRoom(currentRoom, direction):
    new_currentRoom = currentRoom
    for i in rooms:
        if i == currentRoom:
            if direction in rooms[i]:
                new_currentRoom=rooms[i][direction]  #Changes the room
    return new_currentRoom

#Display items
def get_item(currentRoom):
    return rooms[currentRoom]['Item']

#Main Game Code
while (1):

    #Display current status
    item=get_item(currentRoom)
    print('You are in ', currentRoom,'\nInventory:',inventory,"\n",'\nYou see a',item)

    #Player loses the game
    if item=='Choronzon':
        print('Your soul has perished to Choronzon. RIP')
        break

    #Define all possible moves
    direction = input('Enter your move: ')  #Prompt to make move
    if (direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South'):
        direction=direction[3:]
        new_currentRoom = get_new_currentRoom(currentRoom, direction)

        #Invalid move
        if new_currentRoom == currentRoom:
            print('Its blocked off.')

        else:
            currentRoom = new_currentRoom

    #How to grab items
    elif direction==str('get '+item):
        if item in inventory:
            print('You have this.')
        else:
            inventory.append(item)

   #Invalid move
    else:
        print('That train has already left.')

   #Win condition
    if len(inventory)==6:
        print('The Goddess has arrived, Our stars shine eternally. Thank you')
        break
