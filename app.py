"""
Copyright (C) 2025 Ayrik Nabirahni.
This file is part of the Binacle Web App.
Licensed under the GNU AGPL-3.0-or-later.
"""

from flask import Flask, render_template, request, redirect, url_for, session
import requests
from data.data import *
from data.multipliers import *

app = Flask(__name__)
app.secret_key = "binacle_secret_key"  # required for session storage


# --- Core Binacle logic ---

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "types": [t["type"]["name"] for t in data["types"]],
            'sprite_url': data['sprites']['front_default']
        }
    
    return None


def get_move_info(move_name):
    url = f"https://pokeapi.co/api/v2/move/{move_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["type"]["name"]
    return None


def extract_moves(moveset):
    return [m.strip().replace(" ", "-") for m in moveset.split(",") if m.strip()]


def initialize_pokemon(name, moveset_string, is_enemy):
    info = get_pokemon_info(name)
    if not info:
        return None

    pokemon = {"name": info["name"], "types": info["types"], 'sprite_url': info['sprite_url']}
    print(f'got sprite {pokemon['sprite_url']}')

    if not is_enemy:
        moves = extract_moves(moveset_string)
        move_types = [get_move_info(m) for m in moves]
        pokemon["moves"] = moves
        pokemon["move_types"] = move_types

    return pokemon


def calculate_weakness_multiplier(defending_types, attacking_type):
    weakness = 1
    for t in defending_types:
        weakness *= type_defense_dict[t][attacking_type]
    return weakness


# --- Flask routes ---

@app.route("/", methods=["GET", "POST"])
def index():
    """Step 1: Enter 3 friendly Pokémon"""
    if request.method == "POST":
        friendly_team = []
        for i in range(1, 4):
            name = request.form.get(f"name{i}")
            moves = request.form.get(f"moves{i}")

            if not name or not moves:
                return render_template("index.html", error="Please fill out all Pokémon and moves!", binacle_version=version)

            p = initialize_pokemon(name, moves, False)
            if not p:
                return render_template("index.html", error=f"Could not load Pokémon '{name}'. Please check spelling.", binacle_version=version)
            friendly_team.append(p)

        session["friendly_team"] = friendly_team
        session["enemy_list"] = []
        return redirect(url_for("battle"))

    # 🟩 IMPORTANT: Always return something on GET
    return render_template("index.html", binacle_version=version)


@app.route("/battle", methods=["GET", "POST"])
def battle():
    """Step 2: Add enemies one by one, show all after 3"""
    friendly_team = session.get("friendly_team")
    enemy_list = session.get("enemy_list", [])

    if not friendly_team:
        return redirect(url_for("index"))

    # Handle new enemy submission
    if request.method == "POST":
        if "reset_enemies" in request.form:
            # Reset only enemies
            session["enemy_list"] = []
            return redirect(url_for("battle"))

        enemy_name = request.form["enemy_name"]
        enemy = initialize_pokemon(enemy_name, None, True)
        if not enemy:
            return render_template("battle.html", error="Could not load enemy Pokémon!", enemies=enemy_list, binacle_version=version)

        enemy_list.append(enemy)
        session["enemy_list"] = enemy_list

    # Build results for all entered enemies
    all_results = []
    for enemy in enemy_list:
        results = []
        for f in friendly_team:
            for move, move_type in zip(f["moves"], f["move_types"]):
                multiplier = calculate_weakness_multiplier(enemy["types"], move_type)
                results.append({
                    "pokemon": f["name"].title(),
                    "move": move.replace("-", " ").title(),
                    "type": move_type.title(),
                    "multiplier": multiplier
                })
        results.sort(key=lambda r: r["multiplier"], reverse=True)
        all_results.append({"enemy": enemy, "results": results})

    return render_template("battle.html", enemies=enemy_list, all_results=all_results, binacle_version=version, friendly_sprites=[friendly_team[0]['sprite_url'], friendly_team[1]['sprite_url'], friendly_team[2]['sprite_url']])


@app.route("/reset")
def reset():
    """Completely reset (team + enemies)"""
    session.clear()
    return redirect(url_for("index"))


if __name__ == '__main__':
    print('starting flask server...')
    app.run()