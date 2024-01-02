from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# 8105664665  Register
# 8105664625  Not Reigster

path = r"C:\Program Files (x86)\msedgedriver.exe"

# Create Edge options
edge_options = Options()

# Create a WebDriver instance with the specified options and path
driver = webdriver.Edge(service=Service(path), options=edge_options)

try:
    driver.get('https://www.flipkart.com/account/login')

    try:
     
     driver.switch_to.active_element.send_keys("8105664625")
     driver.find_element(By.CSS_SELECTOR,"._1k3JO2").click()
     try:
     
      hold = WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID,'px-captcha')))
      ActionChains(driver).click_and_hold(hold).perform()
      time.sleep(9)
      ActionChains(driver).release().perform()
     except Exception as e:
      print("Hold wala button nahi hai")
     finally:
     try:
       contiune = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Existing User? Log in")))
       print("User is not register")
     except Exception as e:
       print("User Already Exist")       
    except Exception as e:
      print("Error while entering phone number:", e)

except TimeoutException:
    print("Timeout waiting for the page to load.")
except Exception as e:
    print("Error occurred while loading the page:", e)
finally:
    driver.quit()
