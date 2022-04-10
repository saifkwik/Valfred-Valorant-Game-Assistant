import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


def update_results(username):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(
        executable_path="C:\\Users\\Rango\\PycharmProjects\\ESports-Match-Tracker-Service\\chrome_driver\\chromedriver.exe",
        options=options)
    try:
        browser.get(username)
        button = browser.find_element(by=By.CLASS_NAME, value="btn-renew")
        time.sleep(2)
        button.click()
        print('Updating Results')
        return True
    except Exception :
        print('failed')
        return False
        pass

def last_updated(username):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(
        executable_path="C:\\Users\\Rango\\PycharmProjects\\ESports-Match-Tracker-Service\\chrome_driver\\chromedriver.exe",
        options=options)
    browser.get(username)
    html_source = browser.page_source
    browser.close()
    soup = BeautifulSoup(html_source, 'html.parser')
    try:
        a = soup.find_all('p', class_='mt-2 mb-0')
        for data in a[0]:
            b = data.getText().strip()
        print(b)
        return True, b
    except IndexError:
        print('no last updated info found, your initials doesnt match with given username')
        return False

