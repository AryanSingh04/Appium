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

driver.get('https://www.ajio.com/')


try:
    modal = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginAjio")))
    modal.click()
except Exception as e:
    print("Modal not found:", e)
    driver.quit()


try:
    number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    number.send_keys("8108661664")
except Exception as e:
    print("Number field not found:", e)
    driver.quit()


try:
    log = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".signin-container .login-btn")))
    log.click()
except Exception as e:
    print("Login button not found:", e)
    driver.quit()
try:
    New = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,".signup-form>h1")))
    print("User Doesn't exist on Ajio.!")
    
except Exception as e:
    print("User Exist on Ajio.!") 
      
finally:
  driver.quit()
