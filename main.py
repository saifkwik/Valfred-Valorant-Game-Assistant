from src.check_access import check_private
from src.make_public import make_public
from src.config import url, soup
from src.last_updated import update_results, last_updated
from src.input_username import validate_input
from src.get_data import compare_results
from database import saved_match_data, player_name
import time
from data_visualization.bar_chart import bar_chart
from data_visualization.pie_chart import pie_chart


def check_status(url):
    # Check private by check_private
    if check_private(url):
        print(f'The account is Private')
        # if private run make_public
        if make_public(url):
            time_left = 5
            print("Authorization Successful")
            print('Wait 30 secs to load results')
            for countdown in range(5):
                print(f'{time_left}')
                time.sleep(1)
                time_left -= 1

    print("Shadows travelling ")
    update_results(url)
    last_updated(url)
    compare_results()


def main():
    # Input username from the user
    if not validate_input(soup):
        check_status(url)
        bar_chart(saved_match_data, player_name)
        pie_chart(player_name, saved_match_data)
        t = time.perf_counter()
        print(f'Time taken: {t} seconds')


if __name__ == '__main__':
    main()
