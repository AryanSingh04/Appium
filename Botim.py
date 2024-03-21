import time
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Need to add logic for adding the contact and deleting the contact

def capture_element_screenshot(driver: WebDriver,bounds:str, file_name):
    # Get the location and size of the element
    bounds_values = bounds.split("][")
    left, top = map(int, bounds_values[0].strip("[").split(","))
    right, bottom = map(int, bounds_values[1].strip("]").split(","))
    # Take a screenshot of the entire screen
    screenshot = driver.get_screenshot_as_png()
    
    # Crop the screenshot to the element's location and size
    from PIL import Image
    from io import BytesIO
    
    screenshot = Image.open(BytesIO(screenshot))
    element_screenshot = screenshot.crop((left, top, right, bottom))
    
    # Save the element screenshot
    element_screenshot.save(file_name)

def automate_botim(phone_number):
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "appium:platformVersion": "14.0",
        "deviceName": "emulator-5554",
        "automationName": "UIAutomator2",
    }
    url = "http://localhost:4723"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    try:
     driver.terminate_app("im.thebot.messenger")
     time.sleep(1)
     driver.activate_app("im.thebot.messenger")
     WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@resource-id="im.thebot.messenger:id/icon"])[4]'))).click()
     WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="im.thebot.messenger:id/layout_search_bar"]'))).click()
     WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.AutoCompleteTextView[@resource-id="im.thebot.messenger:id/search_src_text"]'))).send_keys(phone_number)
     try:
      WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="im.thebot.messenger:id/contact_avatar_ff"]/android.widget.LinearLayout'))).click()
     except:
        print("User is not on botim.!")
        driver.terminate_app("im.thebot.messenger")
        driver.quit()
        
     last_seen = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="im.thebot.messenger:id/user_state_subtitle_view_chat"]')))
     print("Last Seen:-",last_seen.text)
     WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, ' //android.widget.ImageView[@resource-id="im.thebot.messenger:id/simple_draweeView"]'))).click()
     status = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, ' //android.widget.TextView[@resource-id="im.thebot.messenger:id/tv_value"]')))
     print("Status:-",status.text)
     try:
        vip = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="im.thebot.messenger:id/iv_vip"]')))
        print("User is  verified on botim")
     except:
        print("User is not verified on botim")
       
     WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, ' //android.widget.ImageView[@resource-id="im.thebot.messenger:id/simple_draweeView"]'))).click()
     bounds = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="im.thebot.messenger:id/profile_avatar"]'))).get_attribute('bounds')
     capture_element_screenshot(driver,bounds,f"{phone_number}.png")
     driver.terminate_app("im.thebot.messenger")
    except:
        print("Some Error in app")
