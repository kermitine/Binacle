"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the Binacle project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""


import requests
from data.data import *

friendly_pokemon_list = []
enemy_pokemon_list = []

def get_pokemon_info(pokemon_name): # taken from https://medium.com/@mohamed.mywork/learn-apis-with-pok%C3%A9mon-and-python-7003b35b5ba
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokemon_data = response.json()
        pokemon_info = {
            "name": pokemon_data["name"],
            "height": pokemon_data["height"],
            "weight": pokemon_data["weight"],
            "abilities": [ability["ability"]["name"] for ability in pokemon_data["abilities"]],
            "types": [type_data["type"]["name"] for type_data in pokemon_data["types"]]
        }
        return pokemon_info
    else:
        return None
    

def get_move_info(move_name):
    url = f"https://pokeapi.co/api/v2/move/{move_name.lower()}"
    response = requests.get(url)

    if response.status_code == 200:
        move_data = response.json()
        move_info = {
            "type": move_data["type"]["name"]
        }
        return move_info
    else:
        return None

def extract_moves(moveset):
    moveset = moveset.strip()
    moves = moveset.split(',')
    for index in range(len(moves)):
        moves[index] = moves[index].strip()
        moves[index] = moves[index].replace(' ', '-')
    return moves

def initialize_pokemon(name, moveset_string, is_enemy):
    if is_enemy == True:
        pokemon_dict = { # simplified dictionary
        'name': None,
        'types': [],
        }

        pokemon_info = get_pokemon_info(name)

        pokemon_dict['name'] = pokemon_info['name']
        pokemon_dict['types'] = pokemon_info['types']

        return pokemon_dict

    elif is_enemy == False:
        pokemon_dict = {
        'name': None,
        'types': [],
        'moves': None,
        'move_types': []
        }

        pokemon_info = get_pokemon_info(name)

        pokemon_dict['name'] = pokemon_info['name']
        pokemon_dict['types'] = pokemon_info['types']

        moves = extract_moves(moveset_string)
        pokemon_dict['moves'] = moves
        for move in moves: # get move types
            pokemon_dict['move_types'].append(get_move_info(move)['type'])
        
        return pokemon_dict


def calculate_weakness_multiplier(defending_pokemon_types, attacking_move_type):
    defending_pokemon_dict_list = []
    multipliers = []
    weakness = 1
    for type in defending_pokemon_types:
        defending_pokemon_dict_list.append(type_defense_dict[type])

    for dict in defending_pokemon_dict_list:
        multipliers.append(dict[attacking_move_type])

    for multiplier in multipliers:
        weakness = weakness * multiplier

    return weakness # higher number means move is more effective





for x in range (3): # initialize pokemon
    pokemon_name = input("Enter your pokemon's name: ")
    pokemon_moveset = input("Enter Pokemon's moveset, seperated by commas. (ex: Astonish, Dynamic Punch, Sand Tomb): ")
    friendly_pokemon_list.append(initialize_pokemon(pokemon_name, pokemon_moveset, False))


print(friendly_pokemon_list)

pokemon_number = 'first'
enemy_pokemon_index = 0
done = False
while True:
    if done == True:
        end = input('Enter any letter to exit... ')
        break
    else:


        pokemon_name = input(f"Enter your {pokemon_number} opponent's pokemon's name: ")
        enemy_pokemon_list.append(initialize_pokemon(pokemon_name, None, True))


        highest_weakness = 0
        optimal_pokemon_index = 0
        move_index = 0
        # go through each move for each pokemon. the name of the pokemon and highest overall weakness move will be saved
        for friendly_pokemon_index in range(len(friendly_pokemon_list)):
            for move_type_index in range(len(friendly_pokemon_list[friendly_pokemon_index]['move_types'])):
                current_move_type = friendly_pokemon_list[friendly_pokemon_index]['move_types'][move_type_index]
                weakness = calculate_weakness_multiplier(enemy_pokemon_list[enemy_pokemon_index]['types'], friendly_pokemon_list[friendly_pokemon_index]['move_types'][move_type_index])
                if weakness > highest_weakness:
                    highest_weakness = weakness
                    optimal_pokemon_index = friendly_pokemon_index
                    move_index = move_type_index

        print(f'Best move: {friendly_pokemon_list[optimal_pokemon_index]['moves'][move_index]} ({friendly_pokemon_list[optimal_pokemon_index]['name']}) with effectiveness of {round(highest_weakness, 3)}x')




        if pokemon_number == 'first':
            pokemon_number = 'second'
        elif pokemon_number == 'second':
            pokemon_number = 'third'
        elif pokemon_number == 'third':
            done = True
        enemy_pokemon_index += 1