#Selenium 1
#https://sites.goggle.com/a/chromium.org/chromedriver/downloads
#C:\Program Files (x86)     not(@class)       .map(x => x.wholeText)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from datetime import datetime as ds

import time
import requests
import datetime
import os


PATH_COMPUTER = "C:\Program Files (x86)\chromedriver.exe"
PATH_HOME_PAGE = "https://www.falabella.com.pe/falabella-pe"
PATH_TO_CATEGORIES = '//text-fill[not(@class)]/header[@class="Header-module_header__1UdDW"]//ul[@class="TaxonomyDesktop-module_firstLevelMenu__desktop__2F44_"]//p[not(@class)]'
SPACES = '======================'
PATH1='//header[@class="Header-module_header__1UdDW"]//ul[@class="TaxonomyDesktop-module_firstLevelMenu__desktop__2F44_"]/li//p'
PATH2 = '//header[@class="Header-module_header__1UdDW"]//section[@class="TaxonomyDesktop-module_secondLevelMenuContainer__3ts0K"]/div/section/lu/li[1]/a'
PATH3='//header[@class="Header-module_header__1UdDW"]//ul[@class="TaxonomyDesktop-module_firstLevelMenu__desktop__2F44_"]/li//p'
#/a/@hrfe
TITLE1='Title 1'
TITLE2='Title 2'
TITLE3='Title 3'
BODY1 = 'Body 1'
BODY2 = 'Body 2'
BODY3 = 'Body 3'
driver =webdriver.Chrome(PATH_COMPUTER)

def check_file(file_txt_path, title, body):
    try:
        response_1 = None
        datetime_date = datetime.date.today().strftime('%d-%m-%Y')
        datetime_time = ds.now().strftime('%H:%M:%S')
        if os.path.isfile(file_txt_path):
            with open(file_txt_path) as f:
                lines = f.readlines()
                print(lines)
            response_1 = 'read'
        else:
            with open(file_txt_path, 'w', encoding = 'utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(body)
                f.write('\n\n')
                f.write(f'This file was created the {datetime_date}, at {datetime_time}')
            response_1 = 'created'
    except ValueError as ve:
        print(ve)
    return print(f'File was {response_1}')

def create_foder(path1, path2, today):
    try:
        p_1 = f'{path1}/{path2}'
        p_2 = f'{path1}/{path2}/{today}'
        summary_1 = f'{path1}/summary_1.txt'
        summary_2 = f'{path1}/{path2}/summary_2.txt'
        summary_3 = f'{path1}/{path2}/{today}/summary_3.txt'
        if not os.path.isdir(path1):
            os.mkdir(path1)
        check_file(summary_1, TITLE1, BODY1)
        if not os.path.isdir(p_1):
            os.mkdir(p_1)
        check_file(summary_2, TITLE2, BODY2)
        if not os.path.isdir(p_2):
            os.mkdir(p_2)
        check_file(summary_3, TITLE3, BODY3)
        path_to_folder = f'{path1}/{path2}/{today}'
    except ValueError as ve:
        print(ve)
    return path_to_folder

def create_categories_foder(path1, category):
    try:
        p_1 = f'{path1}/{category}'
        if not os.path.isdir(path1):
            os.mkdir(path1)
        if not os.path.isdir(p_1):
            os.mkdir(p_1)
        path_to_folder = f'{path1}/{category}'
    except ValueError as ve:
        print(ve)
    return path_to_folder

def parse_prices_by_category(link, today):
    try:
        response = requests.get(link)
        if response.status_code == 200:
            notice = response.content.decode('utf-8')
            # parsed = html.fromstring(notice)

            try:
                pass
            except IndexError:
                return
            print(link)
            print(title)
            with open(f'{today}/{title}.txt', 'w', encoding = 'utf-8') as f:
                f.write(title)
                f.write('\n\n')
                f.write(summary)
                f.write('\n\n')
                for p in body:
                    f.write(p)
                    f.write('\n')
        else:
            raise ValueError(f'Error: {response.status_code}')
    except ValueError as ve:
        print(ve)

def parse_home():
    try:
        response = requests.get(PATH_HOME_PAGE)
        if response.status_code == 200:
            driver.get(PATH_HOME_PAGE)
            driver.maximize_window()
            time.sleep(3)
            
            today = datetime.date.today().strftime('%d-%m-%Y')
            falabella_folder = 'fallabella_products'
            f_products_folder = 'products_data'
            folder_1 = create_foder(falabella_folder, f_products_folder, today)
            print(folder_1)
            category_names = driver.find_elements(
                By.XPATH, 
                PATH1
            )
            i = 1
            print(len(category_names))
            # category_names2 = driver.find_element(
            #     By.XPATH,
            #     '//header[@class="Header-module_header__1UdDW"]//ul[@class="TaxonomyDesktop-module_firstLevelMenu__desktop__2F44_"]/li[1]//p'
            # )
            # while i <= len(category_names):
            #     category_names2 = driver.find_element(
            #         By.XPATH,
            #         f'//header[@class="Header-module_header__1UdDW"]//ul[@class="TaxonomyDesktop-module_firstLevelMenu__desktop__2F44_"]/li[{i}]//p'
            #     )
            #     print(category_names2.get_attribute("innerText"))
            #     i +=1
            # print(type(category_names),category_names.get_attribute("innerText"))
            for name in category_names:
                element = name.get_attribute("innerText")
                category_fol = create_categories_foder(folder_1, element)
                # print(SPACES+element, category_fol)
                name.click()
                # print(category_fol)
                sub_category_names = driver.find_elements(
                    By.XPATH,
                    PATH2
                )
                print(sub_category_names)
                for sub_name in sub_category_names:
                    sub_element = sub_name.get_attribute("innerText")
                    print(SPACES+sub_element)
        else:
            raise ValueError(f'Error: {response.status_code}')
        
    except ValueError as ve:
        print(ve)
    driver.quit()

def run():
    parse_home()

if __name__ == '__main__':
    run()