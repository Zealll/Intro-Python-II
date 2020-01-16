from room import Room
from player import Player
import helpers
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [{'name': 'Sword', 'description': 'Long Sword'}, {'name': 'Knife', 'description': 'Kitchen Knife'}]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
gamer = Player('Elan', 'outside')


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True:
    # initial_game = input('Press "Start" to start the game, or "Q" to quit! ').strip()

    # if initial_game.lower() == "start":
    print(f"\n[Current Location]: {gamer.current_room}")
    
    for location in room:
        if location == gamer.current_room:
            print(f"[Room Description]: {room[location]}")
            print('[Items in the room]:')
            for item in room[location].items:
                print(f'\tName: {item["name"]}')
    direction = input('Enter direction -> ').strip().lower()
    command = direction.split(' ')
    if len(command) > 1:
        if command[0] == 'get' or command[0] == 'take':
            new_room_items = []
            room_checker = False
            helpers.on_take(direction, room, gamer, new_room_items, command, room_checker)
        elif command[0] == 'drop':
            new_gamer_items = []
            gamer_checker = False
            helpers.on_drop(direction, room, gamer, new_gamer_items, command, gamer_checker)
    else:
        if direction == 'q':
            break
        elif direction == 'add':
            helpers.room_add_item(direction, room, gamer)
        elif direction == 'e' or direction == 'w' or direction == 's' or direction == 'n':
            helpers.direction_helper(direction, room, gamer)
        elif direction == 'i' or direction == 'inventory':
            print(f"[{gamer.name}'s Inventory]:")
            if len(gamer.items) == 0:
                print('\tNothing in your inventory')
            else:
                for items in gamer.items:
                    print(f"\tName: {items['name']}")
                    print(f"\tDescription: {items['description']}")    
        else:
            print('Command Not Recognized')
        
    # elif initial_game == 'q':
    #     break
# print(' ')        
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
