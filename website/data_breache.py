from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


path = r"C:\Program Files (x86)\msedgedriver.exe"
edge_options = Options()

driver = webdriver.Edge(service=Service(path), options=edge_options)
driver.get('https://haveibeenbreached.com/')
   
   # teamaryansingh04@gmail.com
    # alice@gmail.com
    
def breach(mail):
 try:
  
    email =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, './/input[contains(@placeholder,"email")]')))
 
    email.send_keys(mail)
    email.send_keys(Keys.ENTER)
    try:
     breach_status =  WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, './/p[contains(text(),"Your breach status is")]')))
     total_breach = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, './/p[contains(text(),"Total breaches")]')))
     print("Given Email:",i)
     print(breach_status.text)
     print(total_breach.text)
    except TimeoutException as e:
         print("error")
         print("Given Email:",i)
         print("Your breach status is:Nice")
         print("Total breaches:0")
 except Exception as e:
    print("An error occurred while trying to access the website.")
 finally:
    driver.quit()

i = "alice@gmail.com"
breach(i)
