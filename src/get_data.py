import pprint
import time

from src.config import get_url

from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from selenium import webdriver
from database import collection, get_saved_info, get_player_name

scraped_data = []


def get_data(username):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(
        executable_path="C:\\Users\\Rango\\PycharmProjects\\ESports-Match-Tracker-Service\\chrome_driver\\chromedriver.exe",
        options=options)
    url = get_url(username)[0]
    browser.get(url)
    time.sleep(3)
    html_source = browser.page_source
    browser.close()
    soup = BeautifulSoup(html_source, 'html.parser')

    divtag = soup.find_all('div', class_='match-group')

    v = []
    for data in range(1):
        try:
            v.append(divtag[0].getText().replace('-', ''))
            t = list(v[0].split())
        except IndexError:
            pass
    output = []
    index = 1
    try:
        for count, ele in enumerate(t):
            if ele == 'Competitive':
                # print(index, count)
                output.append(t[count - 1:count + 24])
                index += 1
    except UnboundLocalError:
        pass
    match_number = 1
    for data in output:
        try:
            end_result = data[0]
            match_duration = str(data[2])
            _time = f'{data[4]} {data[3]}'
            team_score = data[5]
            enemy_team_score = data[6]
            result = f'{data[5]} - {data[6]}'
            _map = data[7]
            avg_score = data[8]
            kill = data[10]
            death = data[12]
            assist = data[14]
            kda = f"{kill}/{death}/{assist}"
            kd = data[16]
            avg_damage = data[18]
            hs = data[20]
            first_blood = data[22]

            test = {"Match-Number": match_number, "END_RESULT": end_result, "Match-Duration": match_duration,
                    "Time": _time,
                    "Result": [team_score, enemy_team_score], "Map": _map, "Average_Score": avg_score,
                    "Kills": kill,
                    "Deaths": death,
                    "Assists": assist, "KDA": kda, "KD": kd, "Average_Damage": avg_damage,
                    "Headshot_Percentage": hs,
                    "First_Blood": first_blood}
            res = f'{match_number} match history scraped'
            match_number += 1
            scraped_data.append(test)

        except IndexError:
            pass
    return res


def compare_results(username):
    saved_info =''
    player_name = get_player_name(username)[0]
    try:
        saved_info = get_saved_info(player_name)[0]
    except TypeError:
        pass

    try:
        res = get_data(username)
        print(res)
    except UnboundLocalError:
        pass
    try:
        scraped_value = [scraped_data[0]['Match-Duration'], scraped_data[0]['Time']]
        if scraped_value == saved_info:
            document = collection.find({'player_name': player_name})
            for info in document:
                pprint.pprint(info)
        else:
            # delete existing entry for player
            myquery = {"player_name": player_name}
            e = collection.delete_one(myquery)
            print(e.deleted_count, 'match history cleared')

            # create new entry for the player:
            f = {'player_name': player_name, 'match_history': []}
            y = collection.insert_one(f)
            for history in scraped_data:
                v = collection.update_one({"player_name": player_name}, {"$push": {"match_history": history}})
            document = collection.find({'player_name': player_name})
            for info in document:
                pprint.pprint(info)
    except IndexError:
        pass


# if __name__ == '__main__':
#     compare_results(username)
