from src.check_access import check_private
from src.make_public import make_public
from src.config import get_soup
from src.last_updated import update_results, last_updated
from src.input_username import validate_input, take_input
from src.get_data import compare_results
import time
from database import get_saved_info, get_player_name
from data_visualization.bar_chart import bar_chart
from data_visualization.pie_chart import pie_chart
from report_pdf.report import generate_pdf


def check_status(username):
    url = take_input(username)[0]
    player_name = get_player_name(username)[0]

    # Check private by check_private
    if check_private(username):
        print(f'The account is Private')
        # if private run make_public
        if make_public():
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
    compare_results(username)
    try:
        saved_match_data = get_saved_info(player_name)[1]
    except TypeError:
        pass
    bar_chart(saved_match_data, player_name)
    pie_chart(player_name, saved_match_data)


def main(username):
    url = take_input(username)[0]
    soup = get_soup(url)
    if not validate_input(soup):
        check_status(username)

        t = time.perf_counter()
        print(f'Time taken: {t} seconds')
    generate_pdf(username)

if __name__ == '__main__':
    main('peacemaker#dceu')
