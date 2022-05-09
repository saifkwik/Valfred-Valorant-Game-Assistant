import sys
import time

import selenium
from selenium import webdriver


def make_public():
    print(f'Authorize API access to the account to proceed, Browser will autoclose ')
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Rango\\Downloads\\chromedriver_win32\\chromedriver.exe")

    # URL of the website
    url = "https://auth.riotgames.com/login#client_id=dakgg&redirect_uri=https%3A%2F%2Fdak.gg%2Fauth%2Friotgames%2Fcallback&response_type=code&scope=openid%20offline_access&state=val"

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

# make_public()