#Selenium 1
#https://sites.goggle.com/a/chromium.org/chromedriver/downloads
#C:\Program Files (x86)     not(@class)       .map(x => x.wholeText)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import datetime
import os


PATH_COMPUTER = "C:\Program Files (x86)\chromedriver.exe"
PATH_HOME_PAGE = "https://www.plazavea.com.pe/"
PATH_TO_CATEGORIES = '//*[@id="root"]/header/section/div/div[2]/div[2]/ul//a[@class="root"]'
PATH_TO_CATEGORIES2 = '//*[@id="root"]/header/section/div//a[@class="MainMenu__wrapper__departments__item__link"]/span/span[1]'
SPACES = '======================'


driver =webdriver.Chrome(PATH_COMPUTER)


def parse_prices_by_category():
    pass

def parse_home():
    try:
        response = requests.get(PATH_HOME_PAGE)
        if response.status_code == 200:
            driver.get(PATH_HOME_PAGE)
            time.sleep(3)
            
            today = datetime.date.today().strftime('%d-%m-%Y')
            category_name = driver.find_elements(
                By.XPATH, 
                PATH_TO_CATEGORIES2
            )
            print(category_name)
            
            # for name in category_name:
            #     print(name.text)
        else:
            raise ValueError(f'Error: {response.status_code}')
        driver.quit()
    except ValueError as ve:
        print(ve)

def run():
    parse_home()

if __name__ == '__main__':
    run()