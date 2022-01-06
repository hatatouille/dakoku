import sys
import re
import time
from enum import Enum
import datetime as dt
import urllib.parse
from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

CHROMEDRIVER = "./chromedriver"
chrome_service = fs.Service(executable_path=CHROMEDRIVER)
driver = webdriver.Chrome(service=chrome_service)
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
wait = WebDriverWait(driver, 30, ignored_exceptions=ignored_exceptions)

def access():
    # driver.get("https://p.secure.freee.co.jp/#home/2022/2")
    driver.get("https://accounts.secure.freee.co.jp/login/hr")
    login()
    button_taikin = driver.find_element(by=By.XPATH, value="//*[@id=\"homes\"]/div/div[1]/section/div/div[1]/button[1]")
    if button_taikin.text == "退勤する":
        button_taikin.click()
    print('Done')

def login():
    id = driver.find_element(by=By.ID, value="user_email")
    id.send_keys("<ここにあなたのfreeeログイン用のメールアドレスを入れてください>")

    password = driver.find_element(by=By.XPATH, value="/html/body/div[3]/div/main/div/form/div/div[3]/input[1]")
    password.send_keys("<ここにあなたのfreeeログイン用のパスワードを入れてください>")

    login = driver.find_element(by=By.XPATH, value="//*[@id=\"login-page\"]/main/div/form/div/div[5]/input")
    login.click()
    wait.until(EC.presence_of_all_elements_located)
    return

# mainスレッド
if __name__ == '__main__':
    print("打刻を試みます")
    access()
    quit()
