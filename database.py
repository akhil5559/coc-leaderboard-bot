import json, os

PLAYERS_FILE = "data/players.json"
LEADERBOARD_FILE = "data/leaderboard.json"

def _load_file(filename):
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump({}, f)
    with open(filename, "r") as f:
        return json.load(f)

def _save_file(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

players_data = _load_file(PLAYERS_FILE)
leaderboard_data = _load_file(LEADERBOARD_FILE)

def get_player_data():
    return players_data

def get_leaderboard_data():
    return leaderboard_data

def save_player_data():
    _save_file(PLAYERS_FILE, players_data)

def save_leaderboard_data():
    _save_file(LEADERBOARD_FILE, leaderboard_data)