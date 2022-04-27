from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from src.input_username import take_input


def get_url(username):
    string_input = take_input(username)
    url = string_input[0]
    game_name = string_input[1]
    return url, game_name


def get_soup(url):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(
        executable_path="C:\\Users\\Rango\\PycharmProjects\\ESports-Match-Tracker-Service\\chrome_driver\\chromedriver.exe",
        options=options)
    browser.get(url)
    time.sleep(3)
    html_source = browser.page_source
    browser.close()
    soup = BeautifulSoup(html_source, 'html.parser')
    return soup


# url = url('peacemaker#dceu')[0]
# print(url)
# soup = get_soup(url)
# print(soup)
