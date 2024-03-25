from selenium import webdriver
import requests
import shutil
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time


def asana(email):
    chromedriver_path = r"C:/chromedriver.exe"  
    chrome_options = Options()
    chrome_options.add_argument(r'--user-data-dir=C:\Users\teama\AppData\Local\Google\Chrome\User Data')
    try:
        driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)
        driver.get('https://app.asana.com/-/login?')
        input_email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div[1]/div[2]/div/input')))
        input_email.send_keys(email)
        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div[2]')))
        button.click()
        result = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/h2')))
        if "new" in result.text:
            print("Email is not Registered")
        if "Welcome" in result.text:
            print("Email is  Registered")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Done")
        driver.quit()
