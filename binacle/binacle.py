"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the Binacle project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

version = '0.0.2'

import requests


friendly_pokemon_list = []


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

def initialize_pokemon(name, moveset_string):

    pokemon_dict = {
    'name': None,
    'types': [],
    'moves': None,
    'move_types': []
    }

    pokemon_info = get_pokemon_info(name)

    pokemon_dict['name'] = pokemon_info['name']
    pokemon_dict['types'].append(pokemon_info['types'])

    moves = extract_moves(moveset_string)
    pokemon_dict['moves'] = moves
    for move in moves: # get move types
        pokemon_dict['move_types'].append(get_move_info(move)['type'])
    
    return pokemon_dict


for x in range (3): # initialize pokemon
    pokemon_name = input("Enter your pokemon's name: ")
    pokemon_moveset = input("Enter Pokemon's moveset, seperated by commas. (ex: Astonish, Dynamic Punch, Sand Tomb): ")
    friendly_pokemon_list.append(initialize_pokemon(pokemon_name, pokemon_moveset))



print(friendly_pokemon_list)