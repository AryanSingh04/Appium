from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
path = r"C:\Program Files (x86)\msedgedriver.exe"
edge_options = Options()
driver = webdriver.Edge(service=Service(path), options=edge_options)
driver.get('https://auth.trivago.com/en-IN')

input =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ' //*[@id="email"]')))
input.send_keys("teamaryansingh04@gmail.com")

button =WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/section/div/div/main/div/form/button')))
button.click()
time.sleep(2)
if "register" in driver.current_url:
    print("Account Not Registered")
else:
    print("Account Register")

