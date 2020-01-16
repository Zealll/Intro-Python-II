def direction_helper(direction, room, gamer):
    if direction.lower() == 'n':
        if room[gamer.current_room].n_to == None:
            print('There is no room towards that direction!')
        else:
            for room_name in room:
                if room_name in room[gamer.current_room].n_to.name.lower():
                    print(room_name)
                    gamer.current_room = room_name
                    break
    elif direction.lower() == 's':
        if room[gamer.current_room].s_to == None:
            print('There is no room towards that direction!')
        else:
            for room_name in room:
                if room_name in room[gamer.current_room].s_to.name.lower():
                    print(room_name)
                    gamer.current_room = room_name
                    break
    elif direction.lower() == 'w':
        if room[gamer.current_room].w_to == None:
            print('There is no room towards that direction!')
        else:
            for room_name in room:
                if room_name in room[gamer.current_room].w_to.name.lower():
                    print(room_name)
                    gamer.current_room = room_name
                    break
    elif direction.lower() == 'e':
        if room[gamer.current_room].e_to == None:
            print('There is no room towards that direction!')
        else:
            for room_name in room:
                if room_name in room[gamer.current_room].e_to.name.lower():
                    print(room_name)
                    gamer.current_room = room_name
                    break


def room_add_item(direction, room, gamer):
    item_name = input('Name of the Item -> ')
    item_description = input('Item Description -> ')
    room[gamer.current_room].items.append({'name': item_name, 'description': item_description})


def on_take(direction, room, gamer, new_room_items, command, room_checker):
    for room_items in room[gamer.current_room].items:
        if room_items['name'].lower() == command[1]:
            gamer.items.append(room_items)
            room_checker = True
            print(f'You have picked up a {room_items["name"]}')
        else:
            new_room_items.append(room_items)
    if room_checker == False:
        print('There is no Item with that Name in this room')
    else:
        room[gamer.current_room].items = new_room_items

def on_drop(direction, room, gamer, new_gamer_items, command, gamer_checker):
    for gamer_items in gamer.items:
        if gamer_items['name'].lower() == command[1]:
            room[gamer.current_room].items.append(gamer_items)
            gamer_checker = True
            print(f'You have dropped a {gamer_items["name"]}')
        else:
            new_gamer_items.append(gamer_items)
    if gamer_checker == False:
        print('You don\'t have the spacified item in your inventory!')
    else:
        gamer.items = new_gamer_items