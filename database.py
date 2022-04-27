from src.config import get_url
from pymongo import MongoClient

cluster = "mongodb+srv://rango:ylEEDSikq33TLyKx@cluster0.jbwqp.mongodb.net/valorant?retryWrites=true&w=majority"

client = MongoClient(cluster)

db = client.valorant

collection = db.player_database


def saved_players():
    a = collection.find({}, {'_id': 0, 'player_name': 1})

    h = []
    for j in a:
        h.append(list(j.values())[0])
    return h


def get_player_name(username=''):
    player_name = get_url(username)[1]
    return player_name


def get_saved_info(player_name):
    try:
        t = collection.find({'player_name': player_name})

        saved_match_data = []
        for b in t:
            for k in b.values():
                saved_match_data.append(k)

        match_duration = saved_match_data[2][0]['Time']
        saved_match_time = saved_match_data[2][0]['Match-Duration']
        saved_info = [saved_match_time, match_duration]
        return saved_info, saved_match_data
    except IndexError:
        pass

# b = get_player_name('peacemaker#dceu')
# print(b)
# a = get_saved_info('peacemaker-dceu')
# print(a)
