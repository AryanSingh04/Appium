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
import urllib.parse

path = r"C:\Program Files (x86)\msedgedriver.exe"
edge_options = Options()
edge_options.add_argument("--headless")
driver = webdriver.Edge(service=Service(path), options=edge_options)

def get_coordinates(location):
    formatted_location = urllib.parse.quote_plus(location)
    url = f'https://www.google.com/maps/place/{formatted_location}'
    driver.get(url)
    time.sleep(5)
    current_url = driver.current_url
    url_parts = current_url.split("@")
    if len(url_parts) > 1:
        remaining_url = url_parts[1].split("/")[0]
        parts = remaining_url.split(",")
        if len(parts) >= 3:
         latitude = parts[0] 
         longitude = parts[1]
         zoom_level = parts[2].rstrip('z') 
         print("Latitude:", latitude)
         print("Longitude:", longitude)
         print("Zoom Level:", zoom_level)
        else:
         print("Invalid format of the extracted string.")
    else:
        print("Could not extract the string.")
    driver.quit()
    
get_coordinates("Thakur College of Engineering,Kandivali West, Mumbai")
