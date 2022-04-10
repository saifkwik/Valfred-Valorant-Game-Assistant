import sys
import time

import selenium
from selenium import webdriver


def make_public(url):
    print(f'Authorize API access to the account to proceed, Browser will autoclose ')
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Rango\\PycharmProjects\\ESports-Match-Tracker-Service\\chrome_driver\\chromedriver.exe")

    # URL of the website
    url = ""

    driver.get(url)

    for current_url in range(1, 40):
        try:
            time.sleep(3)
            print('checking')
            get_url = driver.current_url
            if "https://dak.gg/valorant/profile/" in get_url:
                driver.close()
                return True
        except selenium.common.exceptions.InvalidSessionIdException:
            break
        except selenium.common.exceptions.WebDriverException:
            print('Browser force closed')
            sys.exit()
