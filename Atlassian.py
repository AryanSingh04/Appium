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
driver.get('https://id.atlassian.com/login')
try:
   input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
   input.send_keys("erg2570@gmail.com")
   button =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, ' //*[@id="login-submit"]')))
   button.click()
   try:
     sign_up = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signup-submit"]')))
     print("Account Not Found")
   except Exception as e:
     print("Account Found")
except Exception as e:
    print("An error occurred while trying to load the page.")
