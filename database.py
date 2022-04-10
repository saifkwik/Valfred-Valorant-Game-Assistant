from src.config import game_name
from pymongo import MongoClient

cluster = ""

client = MongoClient(cluster)

db = client.valorant

collection = db.player_database


def saved_players():
    a = collection.find({}, {'_id': 0, 'player_name': 1})

    h = []
    for j in a:
        h.append(list(j.values())[0])
    return h


player_name = game_name[0]

saved_info = []
try:
    t = collection.find({'player_name': player_name})

    saved_match_data = []
    for b in t:
        for k in b.values():
            saved_match_data.append(k)

    match_duration = saved_match_data[2][0]['Time']
    saved_match_time = saved_match_data[2][0]['Match-Duration']
    saved_info = [saved_match_time, match_duration]

except IndexError:
    pass

