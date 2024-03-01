from selenium import webdriver
import requests
import shutil
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chromedriver_path = r"C:/chromedriver.exe"  
chrome_options = Options()
chrome_options.add_argument(r'--user-data-dir=C:\Users\teama\AppData\Local\Google\Chrome\User Data')
driver = webdriver.Chrome(service=Service(chromedriver_path), options=chrome_options)

driver.get('https://web.telegram.org')
try:
 time.sleep(2)
 ham = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, " //*[@id='column-left']/div/div/div[1]/div[1]/button")))
 ham.click()
 cont = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="column-left"]/div/div/div[1]/div[1]/button/div[3]/div[4]')))
 cont.click()
 add = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div[2]/button')))
 time.sleep(1)
 add.click()
 NameInput = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div[2]/div[1]/div[1]')))
 NameInput.click()
 NameInput.send_keys("aaj")
 NumberInput =  WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div[3]/div[1]')))
 NumberInput.click()
 NumberInput.send_keys("+918795626393")
 Submit = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div[1]/button[2]')))
 Submit.click()
 time.sleep(1)
 try:
  WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div/div[1]/button[2]')))
  print("User is not on telegram")
 except Exception as e:
   search = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="contacts-container"]/div[1]/div/input')))
   search.send_keys("aaj")
   time.sleep(2)
   WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="contacts"]/a/div[1]'))).click()
   WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="column-center"]/div/div/div[2]/div[1]/div[1]/div/div[1]'))).click()
   WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="column-right"]/div/div/div[1]/div/div[1]/button/div'))).click()
   WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="column-right"]/div/div[2]/div[2]/div/div[3]/div/div/button/div'))).click()
   dele = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[contains(@class,"popup-delete-contact")]//div[@class="popup-buttons"]/button[1]')))
   dele.click()
   time.sleep(5)
   name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="column-right"]//div[@class="profile-name"]')))
   last_seen = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="column-right"]//div[@class="profile-subtitle"]')))
   url = driver.current_url
   uname = url.split('@')[-1] if '@' in url else None
   if uname:
        print("Username:", f"@{uname}")
   else:
        print("No Username")
   try:
    avatars = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="column-right"]//div[contains(@class, "profile-avatars-container")]')))
    imgs = avatars.find_elements("tag name","img")
    os.makedirs("avatar_screenshots", exist_ok=True)
    for index, img in enumerate(imgs):
     img.screenshot(f"avatar_screenshots/avtaar_{index}.png")
    print("Image downloaded successfully.")
   except Exception as e:
      print("No Profile Image")
   print("Name:",name.text)
   print("Last Seen:",last_seen.text)
except Exception as e:
    print("some error",e)
finally:
 print("done")
 driver.quit()
