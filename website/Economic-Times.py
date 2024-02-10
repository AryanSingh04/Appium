from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = r"C:\Program Files (x86)\msedgedriver.exe"
edge_options = Options()
driver = webdriver.Edge(service=Service(path), options=edge_options)

driver.get('https://economictimes.indiatimes.com/')

try:
    log = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/main/header/div/div[2]/div[1]')))
    log.click()
    input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="emailAndMobile"]')))
    input.send_keys("9004879007")
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signInButton"]')))
    button.click()
    try:
        last = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Sign Up")]')))
        print("User is not Register")
    except Exception as e:
        last = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[contains(text(),"Sign In")]')))
        print("User is  Register")
except Exception as e:
    print("some Error occured")

