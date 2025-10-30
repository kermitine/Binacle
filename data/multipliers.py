"""
Copyright (C) 2025 Ayrik Nabirahni. This file
is apart of the Binacle project, and licensed under
the GNU AGPL-3.0-or-later. See LICENSE and README for more details.
"""

normal_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'electric': 1,
    'grass': 1,
    'ice': 1,
    'fighting': 1.6,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 1,
    'bug': 1,
    'rock': 1,
    'ghost': 0.39,
    'dragon': 1,
    'dark': 1,
    'steel': 1,
    'fairy': 1
}

fire_type_defense_multipliers = {
    'normal': 1,
    'fire': 0.63,
    'water': 1.6,
    'electric': 1,
    'grass': 0.63,
    'ice': 0.63,
    'fighting': 1,
    'poison': 1,
    'ground': 1.6,
    'flying': 1,
    'psychic': 1,
    'bug': 0.63,
    'rock': 1.6,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 0.63,
    'fairy': 0.63
}

water_type_defense_multipliers = {
    'normal': 1,
    'fire': 0.63,
    'water': 0.63,
    'electric': 1.6,
    'grass': 1.6,
    'ice': 0.63,
    'fighting': 1,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 1,
    'bug': 1,
    'rock': 1,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 0.63,
    'fairy': 1
}

electric_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'electric': 0.63,
    'grass': 1,
    'ice': 1,
    'fighting': 1,
    'poison': 1,
    'ground': 1.6,
    'flying': 1,
    'psychic': 1,
    'bug': 1,
    'rock': 1,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 0.63,
    'fairy': 1
}

grass_type_defense_multipliers = {
    'normal': 1,
    'fire': 1.6,
    'water': 0.63,
    'electric': 0.63,
    'grass': 0.63,
    'ice': 1.6,
    'fighting': 1,
    'poison': 1.6,
    'ground': 0.63,
    'flying': 1.6,
    'psychic': 1,   
    'bug': 1.6,
    'rock': 1,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 1,
    'fairy': 1
}

ice_type_defense_multipliers = {
    'normal': 1,
    'fire': 1.6,
    'water': 1,
    'electric': 1,
    'grass': 1,
    'ice': 0.63,
    'fighting': 1.6,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 1,   
    'bug': 1,
    'rock': 1.6,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 1.6,
    'fairy': 1
}

fighting_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'electric': 1,
    'grass': 1,
    'ice': 1,
    'fighting': 1,
    'poison': 1,
    'ground': 1,
    'flying': 1.6,
    'psychic': 1.6,   
    'bug': 0.63,
    'rock': 0.63,
    'ghost': 1,
    'dragon': 1,
    'dark': 0.63,
    'steel': 1,
    'fairy': 1.6
}

poison_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'electric': 1,
    'grass': 0.63,
    'ice': 1,
    'fighting': 0.63,
    'poison': 0.63,
    'ground': 1.6,
    'flying': 1,
    'psychic': 1.6,   
    'bug': 0.63,
    'rock': 1,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 1,
    'fairy': 0.63
}

ground_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1.6,
    'electric': 0.39,
    'grass': 1.6,
    'ice': 1.6,
    'fighting': 1,
    'poison': 0.63,
    'ground': 1,
    'flying': 1,
    'psychic': 1,   
    'bug': 1,
    'rock': 0.63,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 1,
    'fairy': 1
}

flying_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'electric': 1.6,
    'grass': 0.63,
    'ice': 1.6,
    'fighting': 0.63,
    'poison': 1,
    'ground': 0.39,
    'flying': 1,
    'psychic': 1,   
    'bug': 0.63,
    'rock': 1.6,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 1,
    'fairy': 1
}

psychic_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'electric': 1,
    'grass': 1,
    'ice': 1,
    'fighting': 0.63,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 0.63,   
    'bug': 1.6,
    'rock': 1,
    'ghost': 1.6,
    'dragon': 1,
    'dark': 1.6,
    'steel': 1,
    'fairy': 1
}

bug_type_defense_multipliers = {
    'normal': 1,
    'fire': 1.6,
    'water': 1,
    'electric': 1,
    'grass': 0.63,
    'ice': 1,
    'fighting': 0.63,
    'poison': 1,
    'ground': 0.63,
    'flying': 1.6,
    'psychic': 1,   
    'bug': 1,
    'rock': 1.6,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 1,
    'fairy': 1
}

rock_type_defense_multipliers = {
    'normal': 0.63,
    'fire': 0.63,
    'water': 1.6,
    'electric': 1,
    'grass': 1.6,
    'ice': 1,
    'fighting': 1.6,
    'poison': 0.63,
    'ground': 1.6,
    'flying': 0.63,
    'psychic': 1,   
    'bug': 1,
    'rock': 1,
    'ghost': 1,
    'dragon': 1,
    'dark': 1,
    'steel': 1.6,
    'fairy': 1
}

ghost_type_defense_multipliers = {
    'normal': 0.39,
    'fire': 1,
    'water': 1,
    'electric': 1,
    'grass': 1,
    'ice': 1,
    'fighting': 0.39,
    'poison': 0.63,
    'ground': 1,
    'flying': 1,
    'psychic': 1,   
    'bug': 0.63,
    'rock': 1,
    'ghost': 1.6,
    'dragon': 1,
    'dark': 1.6,
    'steel': 1,
    'fairy': 1
}

dragon_type_defense_multipliers = {
    'normal': 1,
    'fire': 0.63,
    'water': 0.63,
    'electric': 0.63,
    'grass': 0.63,
    'ice': 1.6,
    'fighting': 1,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 1,   
    'bug': 1,
    'rock': 1,
    'ghost': 1,
    'dragon': 1.6,
    'dark': 1,
    'steel': 1,
    'fairy': 1.6
}

dark_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'electric': 1,
    'grass': 1,
    'ice': 1,
    'fighting': 1.6,
    'poison': 1,
    'ground': 1,
    'flying': 1,
    'psychic': 0.39,   
    'bug': 1.6,
    'rock': 1,
    'ghost': 0.63,
    'dragon': 1,
    'dark': 0.63,
    'steel': 1,
    'fairy': 1.6
}

steel_type_defense_multipliers = {
    'normal': 0.63,
    'fire': 1.6,
    'water': 1,
    'electric': 1,
    'grass': 0.63,
    'ice': 0.63,
    'fighting': 1.6,
    'poison': 0.39,
    'ground': 1.6,
    'flying': 0.63,
    'psychic': 0.63,   
    'bug': 0.63,
    'rock': 0.63,
    'ghost': 1,
    'dragon': 0.63,
    'dark': 1,
    'steel': 0.63,
    'fairy': 0.63
}

fairy_type_defense_multipliers = {
    'normal': 1,
    'fire': 1,
    'water': 1,
    'electric': 1,
    'grass': 1,
    'ice': 1,
    'fighting': 0.63,
    'poison': 1.6,
    'ground': 1,
    'flying': 1,
    'psychic': 1,   
    'bug': 0.63,
    'rock': 1,
    'ghost': 1,
    'dragon': 0.39,
    'dark': 0.63,
    'steel': 1.6,
    'fairy': 1
}

type_defense_dict = {
    'normal': normal_type_defense_multipliers,
    'fire': fire_type_defense_multipliers,
    'water': water_type_defense_multipliers,
    'electric': electric_type_defense_multipliers,
    'grass': grass_type_defense_multipliers,
    'ice': ice_type_defense_multipliers,
    'fighting': fighting_type_defense_multipliers,
    'poison': poison_type_defense_multipliers,
    'ground': ground_type_defense_multipliers,
    'flying': flying_type_defense_multipliers,
    'psychic': psychic_type_defense_multipliers,
    'bug': bug_type_defense_multipliers,
    'rock': rock_type_defense_multipliers,
    'ghost': ghost_type_defense_multipliers,
    'dragon': dragon_type_defense_multipliers,
    'dark': dark_type_defense_multipliers,
    'steel': steel_type_defense_multipliers,
    'fairy': fairy_type_defense_multipliers
}