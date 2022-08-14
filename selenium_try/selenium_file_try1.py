#Selenium 1
#https://sites.goggle.com/a/chromium.org/chromedriver/downloads
#C:\Program Files (x86)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time




PATH_COMPUTER = "C:\Program Files (x86)\chromedriver.exe"
PATH_PAGE = "https://es.investing.com/crypto/bitcoin"
BIT_COIN_VALUE = '//*[@id="last_last"]'
BIT_COIN_RISE = '//*[@id="fullColumn"]/div[6]/div/div[1]/div[2]/span[2]'
BIT_COIN_RISE_PERCEN= '//*[@id="fullColumn"]/div[6]/div/div[1]/div[2]/span[4]'
SPACES = "==========================="

def print_with_spaces(argument_to_print):
    response = print(
        SPACES + 
        argument_to_print + 
        SPACES
    )
    return response

driver =webdriver.Chrome(PATH_COMPUTER)
driver.get(PATH_PAGE)

time.sleep(5)
procces1 = "first procces" 
procces2 = "second procces" 
procces3 = "third procces" 

value = driver.find_element(
    By.XPATH, 
    BIT_COIN_VALUE
)

rise = driver.find_element(
    By.XPATH, 
    BIT_COIN_RISE
)

percen = driver.find_element(
    By.XPATH, 
    BIT_COIN_RISE_PERCEN
)
print(type(value))
print_with_spaces(value.text)
print_with_spaces(procces2)
print_with_spaces(rise.text)
print_with_spaces(procces3)
print_with_spaces(percen.text)

driver.quit()

# time.sleep(5)

# precioBTC = driver.find_element_by_xpath('//*[@id="last_last"]')

# print('Precio del Bitcoin: '+ precioBTC.text)

# driver.quit()


# options = webdriver.ChromeOptions()

# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
# options.add_argument('--headless')



