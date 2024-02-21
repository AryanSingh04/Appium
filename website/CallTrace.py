from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def number_loc(num):
    path = r"C:\Program Files (x86)\msedgedriver.exe"
    edge_options = Options()
    driver = webdriver.Edge(service=Service(path), options=edge_options)
    driver.get(f'https://calltracer.in/track-{num}-current-location/#gpsLocation')
    print("Number:",num)
    sim = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/table[1]/tbody/tr[4]/td[2]/a')))
    print("Carrier:",sim.text)
    city =  WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/table[1]/tbody/tr[5]/td[2]/a')))
    print("City:",city.text)
    country =   WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ' /html/body/div[1]/div/table[1]/tbody/tr[17]/td[2]')))
    print("Country:",country.text)
    driver.quit()
# Example usage:
number =9445278432
number_loc(number)
