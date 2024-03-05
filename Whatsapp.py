import time
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# // Works on phone having google dialer probably;
def capture_element_screenshot(driver: WebDriver, bounds: str, file_name):
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
def automate_whatsapp(country_code, phone_number,naam):
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
        name_input.send_keys(naam)
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
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH,
                                                '//android.widget.ImageButton[@content-desc="Navigate up"]'))).click()
            search = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Search"]'))
            )
            search.click()

            search_input = driver.find_element(by=AppiumBy.XPATH,
                                               value='//android.widget.EditText[@resource-id="com.whatsapp:id/search_input"]')
            search_input.send_keys(phone_number)

            name = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.ImageView[@content-desc="{naam}"]'))
            )
            name.click()

            more = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Info"]'))
            )
            more.click()

            s = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.whatsapp:id/contact_title"]')))
            print(s.text)
            status = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/status')))
            print(status.text)
            try:
                lastSeen = WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/contact_chat_status')))
                print(lastSeen.text)
            except Exception as e:
                print(f"No Data for lastSeen")
            profile_picture_element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/wds_profile_picture')))
            profile_picture_element.click()
            try:
                bounds = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, 'com.whatsapp:id/picture_animation'))).get_attribute(
                    'bounds')
                capture_element_screenshot(driver, bounds, f"{s.text}.png")
                profile_picture_element.take_snapshot()

            except Exception as e:
                print("No profile photo found")

            finally:
                driver.press_keycode(4)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH,
                         '//androidx.appcompat.widget.LinearLayoutCompat'))).click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="com.whatsapp:id/title" and @text="View in address book"]'))).click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH,
                         '//android.widget.ImageView[@content-desc="More options"]'))).click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH,
                         '//android.widget.TextView[@resource-id="com.google.android.contacts:id/title" and @text="Delete"]'))).click()
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH,
                         '//android.widget.Button[@resource-id="android:id/button1"]'))).click()
                driver.terminate_app('com.whatsapp')
                driver.terminate_app('com.google.android.dialer')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        if 'driver' in locals():
            driver.quit()
            print("Script executed")


# Example usage:
country_code = "+91"
phone_number_to_search = "8108665665"
automate_whatsapp(country_code, phone_number_to_search,"appium")
