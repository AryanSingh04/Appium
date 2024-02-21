from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
edge_profile_directory = r"C:\Users\teama\AppData\Local\Microsoft\Edge\User Data\Profile 5"
path = r"C:\Program Files (x86)\msedgedriver.exe"
edge_options = Options()
# aryanrrsingh.04@gmail.com 
# teamaryansingh04@gmail.com 
driver = webdriver.Edge(service=Service(path), options=edge_options)
driver.get('https://unocoin.com/in/home')

def uno_coin(num):
    
 try:
    input =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div[2]/label/div/div/div/input')))
    input.send_keys(num)
    passw =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div[3]/label/div/div/div[1]/input')))
    passw.send_keys("Inbsttfr@01")
    button =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div[4]/button')))
    button.click()
    try:
     red = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[2]/div/div[2]/label/div/div[2]')))
     print("User Not Exist!")
    except Exception as e:
        print("User Exist!")
 except Exception as e:
    print("Some Error")
 finally:
    driver.quit()
numm=9004873060
uno_coin(numm)
