import time

from database import saved_players
from src.last_updated import update_results, last_updated
from src.config import url
from src.get_data import compare_results

def exisiting_players():
    saved_playernames = saved_players()
    print(saved_playernames)
    print("Shadows travelling ")
    update_results(url)
    last_updated(url)
    compare_results()
    t2 = time.perf_counter()
    print(f'Time taken: {t2} seconds')
exisiting_players()