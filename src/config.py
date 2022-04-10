from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup
from selenium import webdriver
import time
from src.input_username import take_input

string_input = take_input()
url = string_input[0]
game_name = string_input[1]

options = Options()
options.headless = True
browser = webdriver.Chrome(
    executable_path="C:\\Users\\Rango\\PycharmProjects\\ESports-Match-Tracker-Service\\chrome_driver\\chromedriver.exe",
    options=options)


def get_soup(url):
    browser.get(url)
    time.sleep(3)
    html_source = browser.page_source
    browser.close()
    soup = BeautifulSoup(html_source, 'html.parser')
    return soup


soup = get_soup(url)
# print(soup)
