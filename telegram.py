from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    "platformName": "Android",
    "appium:platformVersion": "14.0",
    "deviceName": "emulator-5554",
    "automationName": "UIAutomator2",
}

url = "http://localhost:4723"
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.set_app_language('en')
driver.set_app_locale('US')

def telegram_search(phone_number, contact_name):
    try:
        driver.terminate_app('org.telegram.messenger.web')
        telegram = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Telegram"]')))
        telegram.click()

        search_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.XPATH, '//android.widget.ImageButton[@content-desc="Search"]/android.widget.ImageView')))
        search_button.click()

        search_bar = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@text="Search"]')))
        search_bar.send_keys("+91", phone_number)
        # driver.press_keycode(67)
        try:
            add_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, '//android.widget.FrameLayout[@text="Add +91 %s"]' % phone_number)))
            add_button.click()

            name_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH,
                                                '//android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.EditText')))
            name_button.send_keys(contact_name)

            ad_button = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Create Contact"]')))
            ad_button.click()

            try:
                invite = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located(
                        (AppiumBy.XPATH, '//android.widget.TextView[@text="Invite to Telegram"]')))
                print("User Not Exist")
            except Exception as e:
                print("User Exist")

            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.view.ViewGroup')))
            print(result.text)

        except Exception as e:
            print("User Exist")
            result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.CLASS_NAME, 'android.view.ViewGroup')))
            print(result.text)

    except Exception as e:
        print(f"Some Error Occurred While Opening Telegram: {e}")

    finally:
        try:
          
            driver.terminate_app('org.telegram.messenger.web')

        finally:
           
            driver.quit()


telegram_search("7304886870", "Ap")
