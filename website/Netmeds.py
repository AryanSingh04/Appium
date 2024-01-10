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

# 8105664625 Not Register!

driver = webdriver.Edge(service=Service(path), options=edge_options)
driver.get('https://www.netmeds.com/customer/account/login')

try:
    input_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "loginfirst_mobileno")))
    input_field.send_keys("8105664625")
    button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".form-check .btn-signpass")))
    button.click()
    time.sleep(10)
    try:
        email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "reg_email")))
        print("User does not exist on NetMeds")
    except Exception as e:
         print("User exists on NetMeds")
except TimeoutException:
    print("Timeout waiting for elements.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    driver.quit()
