from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_whatsapp(country_code, phone_number):
    cap: Dict[str, Any] = {
        "platformName": "Android",
        "appium:platformVersion": "14.0",
        "deviceName": "emulator-5554",
        "automationName": "UIAutomator2",
    }

    url = "http://localhost:4723"

    try:
        driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
        driver.set_app_language('en')
        driver.set_app_locale('US')
        driver.terminate_app('com.whatsapp')
        driver.activate_app('com.whatsapp')

        new_chat_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="New chat"]'))
        )
        new_chat_button.click()

        save_contact_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH,
                                            '//android.widget.TextView[@resource-id="com.whatsapp:id/contactpicker_row_name" and @text="New contact"]')))
        save_contact_button.click()
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.whatsapp:id/first_name_field"]')))
        name_input.send_keys("Appium Save")
        code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.whatsapp:id/country_code_field"]')))
        code_input.send_keys(country_code)
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.whatsapp:id/phone_field"]')))
        phone_input.send_keys(phone_number)

        try:
            invite_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH,
                                                '//android.widget.TextView[@resource-id="com.whatsapp:id/number_on_whatsapp_action"]')))
            print("User is not on Whatsapp")
           
            driver.terminate_app('com.whatsapp')

        except Exception as e:
            save_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH,
                                                '//android.widget.Button[@resource-id="com.whatsapp:id/keyboard_aware_save_button"]')))
            save_button.click()
            search = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Search"]'))
            )
            search.click()

            search_input = driver.find_element(by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@resource-id="com.whatsapp:id/search_src_text"]')
            search_input.send_keys(phone_number)

            name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/contactpicker_row_name'))
            )

            driver.find_element(by=AppiumBy.XPATH, value='(//android.widget.FrameLayout[@resource-id="com.whatsapp:id/contact_selector"])[1]').click()

            more = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Info"]'))
                )
            more.click()

            s = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.whatsapp:id/contact_title"]')))
            print(s.text)

            try:
                    lastSeen = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/contact_chat_status')))
                    print(lastSeen.text)

            except Exception as e:
                    print(f"An error occurred: {str(e)}")

            status = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/status')))
            print(status.text)

            profile_picture_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/wds_profile_picture')))
            profile_picture_element.click()
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/picture_animation')))
                driver.save_screenshot("temp.png")
                navigate_back = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')))


            except Exception as e:
                print("No profile photo found")
            finally:
                 driver.terminate_app('com.whatsapp')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        if 'driver' in locals():
            driver.quit()
            print("Script executed")

# Example usage:
country_code = "+91"
phone_number_to_search = "9702640525"
automate_whatsapp(country_code, phone_number_to_search)

