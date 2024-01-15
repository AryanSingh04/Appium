from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import requests


edge_profile_directory = r"C:\Users\teama\AppData\Local\Microsoft\Edge\User Data\Profile 5"
path = r"C:\Program Files (x86)\msedgedriver.exe"
edge_options = Options()
edge_options.add_argument("user-data-dir=" + edge_profile_directory)
driver = webdriver.Edge(service=Service(path), options=edge_options)
driver.get('https://outlook.live.com/people/0/')


def scrape_LinkedIn(email,name):
 try:
    first_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="feature-oc387eee"]/div/div/div[1]/div/div[3]/div[1]/a')))
    
    first_element.click()
    
    
    WebDriverWait(driver, 20).until(lambda driver: len(driver.window_handles) > 1)

   
    driver.switch_to.window(driver.window_handles[1])

  
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="355fbd79-3ba2-4554-8f2d-0300fde91f30"]'))).click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="innerRibbonContainer"]/div[1]/div/div/div/div[1]/div/span/button[1]'))).click()
    # Adding contact in outloook
    name_input = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, '//input[contains(@aria-label, "Last name")]')))
    name_input.send_keys(name)
    emailInput =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//input[contains(@aria-label,"Email address 1")]')))
    emailInput.send_keys(email)
    button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(@data-automation,"LPESave")]')))
    button.click()
    # end adding contact
    # searching of that contact
    search = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@role="searchbox" and @placeholder="Search"]')))
    search.click()
    search.send_keys(name)
    
    put = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, f'//li[contains(@aria-label, "{email}")]')))
    put.click()
    
    linkedIn =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'LPC_Header_TabBar_LinkedIn')))
    linkedIn.click()
    try:
     displayNAme = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@class, "displayName")]')))
     print("Name:",displayNAme.text)
    
     title =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@data-log-name, "Title")]')))
     print("Title:",title.text)
     about =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[contains(@data-log-name, "AboutInfo")]')))
  
     print("About:",about.text)
     job1 =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(@data-testid, "employmentInfo_0")]')))
     print("Job 1:",job1.text)
     job2 =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(@data-testid, "employmentInfo_1")]')))
     print("Job 2:",job2.text)
     education1 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[contains(@data-testid, "educationInfo_0")]')))
     print("Education 1:",education1.text)
     try:
      img = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//img[contains(@class, "ms-Image-image is-loaded ms-Image-image--contain ms-Image-image--portrait")]')))
      url = img.get_attribute("src")
      if url:
        # Send an HTTP request to get the image content
        img_data = requests.get(url).content

        # Save the image locally
        with open(f'{name}.png', "wb") as img_file:

            img_file.write(img_data)

      else:
        print("Image URL is empty.")
     except Exception as e:
        print("Something went wrong or images does not exist.!")
    except Exception as e:
     print("No more information available.",e)
 except Exception as e:
    print("Error Occured",e)
