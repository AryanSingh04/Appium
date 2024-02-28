import time
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def automate_whatsapp(phone_number):
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "appium:platformVersion": "14.0",
        "deviceName": "emulator-5554",
        "automationName": "UIAutomator2",
    }
    url = "http://localhost:4723"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    try:
        driver.terminate_app('com.whatsapp')
        driver.activate_app('com.whatsapp')
        new_chat_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="New chat"]'))
        )
        new_chat_button.click()
        search = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Search"]'))
        )
        search.click()

        search_input = driver.find_element(by=AppiumBy.XPATH,
                                           value='//android.widget.EditText[@resource-id="com.whatsapp:id/search_src_text"]')
        search_input.send_keys(phone_number)
        try:
         chat = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.whatsapp:id/chat"]'))
         )
         chat.click()
         WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.LinearLayout[@resource-id="com.whatsapp:id/conversation_contact"]'))
         ).click()
         s = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located(
            (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.whatsapp:id/contact_title"]')))
         print(f"search:-{s.text}")
         try:
          status = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/status')))
          print(status.text)
         except Exception as e:
          print("No Status")
         print("Link to chat", f"https://wa.me/+91{phone_number}")
         profile_picture_element = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/wds_profile_picture')))
         profile_picture_element.click()
         try:
             bounds = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/picture_animation'))).get_attribute('bounds')
             capture_element_screenshot(driver,bounds,f"{s.text}.png")
             profile_picture_element.take_snapshot()
             navigate_back = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located(
                     (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')))

         except Exception as e:
             print("No profile photo found")

        except Exception as e:
            print(f"{phone_number} is not on WhatsApp")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        # driver.terminate_app('com.whatsapp')
        driver.quit()
        print("Script executed")


phone_number_to_search = "8108665665"
# 9004896605
# 9004679009
# 9004679009
automate_whatsapp(phone_number_to_search)
