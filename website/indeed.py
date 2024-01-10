from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def perform_registration(email):
    path = r"C:\Program Files (x86)\msedgedriver.exe"
    edge_options = Options()

    driver = webdriver.Edge(service=Service(path), options=edge_options)
    driver.get('https://secure.indeed.com/auth')

    try:
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="ifl-InputFormField-ihl-useId-passport-webapp-1"]')))
        email_input.send_keys(email)

        submit_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="emailform"]/button')))
        submit_button.click()

        status_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="passpage-container"]/main/div/div/div[2]/div/h1')))
        
        if "Create your account" in status_message.text:
            print("Account not created.")
        else:
            print("Account Registered")

    except TimeoutException:
        print("Timeout occurred. Element not found or page did not load within the specified time.")

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        driver.quit()

# Example usage:

email_input = "demo1@gmail.com"
perform_registration(email_input)
