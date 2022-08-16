#Selenium 1
#https://sites.goggle.com/a/chromium.org/chromedriver/downloads
#C:\Program Files (x86)     not(@class)       .map(x => x.wholeText)

from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ExpCon
from selenium.webdriver.support.ui import WebDriverWait
from datetime import datetime as ds

# from .folder_file_create import Creation

import time
import requests
import datetime
import os


PATH_COMPUTER = "C:\Program Files (x86)\chromedriver.exe"
PATH_HOME_PAGE = "https://simple.ripley.com.pe/"
CATEGORY_MENU = '//*[@id="ripley-sticky-header"]/section/nav/div/a'
SPACES = '======================'
PATH_CATEGORIES = '//*[@id="ripley-sticky-header"]/div/div/div/nav/div/div/section/div[1]/a'
PATH_EACH_CATEGORY = '//*[@id="ripley-sticky-header"]/div/div/div/nav/div/div/section/div[1]/a[{}]' 
PATH_SUBCATEGORIES = '//*[@id="ripley-sticky-header"]/div/div/div/nav/div/div[2]/div[2]/div/ul/li/a[1]'
PATH_EACH_SUB_CATEGORY = '//*[@id="ripley-sticky-header"]/div/div/div/nav/div/div[2]/div[2]/div/ul[{}]/li/a[1]'
ENTER_SUB_CATEGORY = '//*[@id="ripley-sticky-header"]/div/div/div/nav/div/div[2]/div[2]/div/ul[{}]/li/a[1]/@hrfe'
COME_BACK_BUTTON='//*[@id="ripley-sticky-header"]/div/div/div/nav/div/div[2]/div[1]/div/a[1]'
#//*[@id="ripley-sticky-header"]/div/div/div/nav/div/div[2]/div[2]/div/ul[1]/li
NOTIF_BUTTON_NO = '//*[@id="onesignal-slidedown-cancel-button"]'
PRODUCT_CONTAINER = 'section[@class="catalog-grid"]/div/div/div/a/div[2]/div'
PRODUCT_IMAGE = 'section[@class="catalog-grid"]/div/div/div/a/div[2]/div[]'
PRODUCT_INFO = '//*[@id="catalog-page"]/div//section/div[@class="row"]/div[@class="catalog-container"]/div[{}]//div{}'
PRODUCT_NAME = '[@class="catalog-product-name-container"]//span'
PRODUCT_DETAILS = '[@class="catalog-product-details__name"]'
PRODUCT_RATING = '[@class="product-rating product-rating-small"]/span[1]/span[1]'
PRODUCT_PRICES = '[@class="catalog-product-details__prices"]/div/ul/li'
PRODUCT_DISCOUNT = '[@class="catalog-product-details__discount-tag"]'
# '//*[@id="catalog-page"]/div/div[2]/div[3]/section/div/div/div[{}]/a/div[2]/div{}'
#//*[@id="catalog-page"]/div/div[2]/div[3]/section
# //*[@id="catalog-page"]/div/div[2]/section/div/div/div[1]
#'[@class="catalog-product-name-container"]/div[1]/div/span'
#//*[@id="catalog-page"]/div/div[2]/div[3]/section/div/div/div[1]/div
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
                # print(lines)
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

def create_product_info(file_path, pr_name, pr_brand, pr_rating, pr_price):
    try:
        response_1 = None
        title = pr_name.replace(
            '¿', ''
        ).replace(
            '\"', ''
        ).replace(
            '“', ''
        ).replace(
            '?', ''
        ).replace(
            '/', '-'
        ).replace(
            '!', ''
        )
        datetime_date = datetime.date.today().strftime('%d-%m-%Y')
        datetime_time = ds.now().strftime('%H:%M:%S')
        txt_path = f'{file_path}/{title}.txt'
        if os.path.isfile(txt_path):
            with open(txt_path) as f:
                lines = f.readlines()
                # print(lines)
            response_1 = 'read'
        else:
            with open(txt_path, 'w', encoding = 'utf-8') as f:
                f.write('Product name:')
                f.write('\n')
                f.write(pr_name)
                f.write('\n\n')
                f.write('Product brand:')
                f.write('\n')
                f.write(pr_brand)
                f.write('\n\n')
                f.write('Product rating:')
                f.write('\n')
                f.write(pr_rating)
                f.write('\n\n')
                f.write('Product price:')
                f.write('\n')
                f.write(pr_price)
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

def wait_somethin_xpath(wait_object: str, action: int, sleep_t: int):
    wait_dv = WebDriverWait(
        driver, 
        30
    )
    
    a = None
    if action == 1:
        a = wait_dv.until(
            ExpCon.presence_of_element_located((
                By.XPATH,
                wait_object
            ))
        )
    elif action == 2:
        a = wait_dv.until(
            ExpCon.presence_of_all_elements_located((
                By.XPATH,
                wait_object
            ))
        )
    if not sleep_t == 0:
        time.sleep(sleep_t)
    # print(a)
    return a

def open_new_tab(new_tab: str, tab_to: int):
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[tab_to])
    driver.get(new_tab)

def close_switch_tab(tab_to: int):
    driver.close()
    # if tab_to > 0:
    driver.switch_to.window(driver.window_handles[tab_to])
    # else:
    #     pass
    time.sleep(1)

def get_product_info(path):
    time.sleep(2)
    # product_container = wait_somethin_xpath(PRODUCT_CONTAINER, 2, 0)
    i = 1
    name = 'None'
    detail = 'None'
    rating = 'None'
    price = 'None'
    discount = 'None'
    # print(len(product_container))
    while i <= 4: #to change how many products is going to read in the page
        wait_somethin_xpath(PRODUCT_INFO.format(i, PRODUCT_NAME), 1, 0)
        each_name = driver.find_element(
            By.XPATH,
            PRODUCT_INFO.format(i, PRODUCT_NAME)
        )
        name = each_name.text
        wait_somethin_xpath(PRODUCT_INFO.format(i, PRODUCT_DETAILS), 1, 0)
        each_detail = driver.find_element(
            By.XPATH,
            PRODUCT_INFO.format(i, PRODUCT_DETAILS)
        )
        detail = each_detail.text
        wait_somethin_xpath(PRODUCT_INFO.format(i, PRODUCT_RATING), 1, 0)
        each_rating = driver.find_element(
            By.XPATH,
            PRODUCT_INFO.format(i, PRODUCT_RATING)
        )
        rating = each_rating.text
        wait_somethin_xpath(PRODUCT_INFO.format(i, PRODUCT_PRICES), 1, 0)
        each_price = driver.find_element(
            By.XPATH,
            PRODUCT_INFO.format(i, PRODUCT_PRICES)
        )
        price = each_price.text
        # if wait_somethin_xpath(PRODUCT_INFO.format(i, PRODUCT_DISCOUNT), 1, 0):
        #     each_discount = driver.find_element(
        #         By.XPATH,
        #         PRODUCT_INFO.format(i, PRODUCT_DISCOUNT)
        #     )
        #     discount = each_discount.text
        # time.sleep(1)
        print(f'object {i}','\n\n')
        print(name, detail, rating, price)
        create_product_info(path, detail, name, rating, price)
        i+=1
    time.sleep(1)
        
   

def parse_home():
    try:
        response = requests.get(PATH_HOME_PAGE)
        if response.status_code == 200:
            driver.get(PATH_HOME_PAGE)
            driver.maximize_window()
            # driver.current_window_handle
            # main_tab = driver.window_handles[0]
            # # assert len(main_tab) == 1
            # print(len(main_tab))
            time.sleep(5)
            wait_somethin_xpath(CATEGORY_MENU, 1, 1)
            wait_somethin_xpath(NOTIF_BUTTON_NO, 1, 1)
            notif_button_no = driver.find_element(
                By.XPATH,
                NOTIF_BUTTON_NO
            )
            notif_button_no.click()
            today = datetime.date.today().strftime('%d-%m-%Y')
            falabella_folder = 'ripley_products'
            f_products_folder = 'products_data'
            category_menu = driver.find_element(
                By.XPATH,
                CATEGORY_MENU
            )
            category_menu.click()
            categories_located = wait_somethin_xpath(
                PATH_CATEGORIES, 
                2, 
                1
            )
            category_names = driver.find_elements(
                By.XPATH, 
                PATH_CATEGORIES
            )
            i = 1
            # print(category_names,'\n\n', categories_located)
            folder_1 = create_foder(
                falabella_folder, 
                f_products_folder, 
                today,   
            )
            while i <= 2:#len(categories_located): #to change how many categories ar going to be read
                # print(i)
                text = PATH_EACH_CATEGORY.format(i)
                wait_somethin_xpath(text, 1, 1)
                each_category = driver.find_element(
                    By.XPATH,
                    PATH_EACH_CATEGORY.format(i)
                )
                # print(text, each_category)
                element_1 = each_category.get_attribute("innerText")
                name_element = each_category.text
                # print(element_1, name_element)
                category_fol = create_categories_foder(folder_1, element_1)
                # print(category_fol)
                each_category.click()
                time.sleep(1)
                sub_cate_loc = wait_somethin_xpath(PATH_SUBCATEGORIES, 2, 1)
                i_1 = 1
                while i_1 <= 3:#len(sub_cate_loc): #to change how many sub categories are going to be read
                    time.sleep(2)
                    print(i_1)
                    path_sub_categ = PATH_EACH_SUB_CATEGORY.format(i_1)
                    # wait_somethin_xpath(COME_BACK_BUTTON, 1, 5)
                    each_subcategories = driver.find_element(
                        By.XPATH,
                        path_sub_categ
                    )
                    element_2 = each_subcategories.get_attribute("innerText")
                    # print(element_2)
                    sub_category_fol = create_categories_foder(category_fol, element_2)
                    print(sub_category_fol)
                    link_new_tab = each_subcategories.get_attribute('href')
                    # print(link_new_tab)
                    open_new_tab(link_new_tab, 1)

                    get_product_info(sub_category_fol)
                    # wait_somethin_xpath(PRODUCT_INFO.format(i, PRODUCT_DISCOUNT), 1, 0)
                    # time.sleep(5)
                    
                    close_switch_tab(0)
                    time.sleep(1)
                    # driver.close()
                    # driver.switch_to.window(driver.window_handles[0])
                    
                    i_1 += 1
                wait_somethin_xpath(COME_BACK_BUTTON, 1, 1)
                
                come_back = driver.find_element(
                    By.XPATH,
                    COME_BACK_BUTTON
                )
                come_back.click()
                time.sleep(1)
                i += 1
        else:
            raise ValueError(f'Error: {response.status_code}')
        
    except ValueError as ve:
        print(ve)
    driver.quit()

def run():
    parse_home()

if __name__ == '__main__':
    run()