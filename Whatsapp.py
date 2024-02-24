from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_whatsapp(phone_number):
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "appium:platformVersion": "8.0",
        "deviceName": "emulator-5554",
        "automationName": "UIAutomator2",
    }

    url = "http://localhost:4723"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    try:
        # driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        driver.set_app_language('en')
        driver.set_app_locale('US')
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
         profile_picture_element = WebDriverWait(driver, 10).until(
             EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/wds_profile_picture')))
         profile_picture_element.click()
         try:
             WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/picture_animation')))
             driver.save_screenshot(f"{s.text}.png")
             navigate_back = WebDriverWait(driver, 10).until(
                 EC.presence_of_element_located(
                     (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')))
             navigate_back.click()

         except Exception as e:
             print("No profile photo found")
         print("Link to chat",f"https://wa.me/{s.text}")
        except Exception as e:
            print(f"{phone_number} is not on WhatsApp")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        driver.terminate_app('com.whatsapp')
        driver.quit()
        print("Script executed")


phone_number_to_search = "8108665665"
# 9004896605
# 9004679009
# 9004679009
automate_whatsapp(phone_number_to_search)
