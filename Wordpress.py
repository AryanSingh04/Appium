from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# demo04@gmail.com [Registered]
# demo02@gmail.com [Not Registered]

path = r"C:\Program Files (x86)\msedgedriver.exe"
edge_options = Options()

driver = webdriver.Edge(service=Service(path), options=edge_options)
driver.get('https://wordpress.com/log-in/')
try:
  email =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="usernameOrEmail"]')))
  email.send_keys("demo04@gmail.com")
  button =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="primary"]/div/main/div[2]/div/form/div[1]/div[2]/button')))
  button.click()
  try:
   message =  WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="primary"]/div/main/div[2]/div/form/div[1]/div[1]/div[1]')))
   crate_new = message.find_element(By.XPATH, './/a[contains(text(), "create a new account")]')
   print("User is Not Registered on Wordpress.")
  except Exception as e:
      print("User is Registered on Wordpress.")
except Exception as e:
    print("An error occurred while trying to access the page: ", str(e))
