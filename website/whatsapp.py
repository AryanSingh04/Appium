from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def get_contact_info(phone_number):
    path = r"C:\Program Files (x86)\msedgedriver.exe"
    edge_options = Options()

    driver = webdriver.Edge(service=Service(path), options=edge_options)
    driver.get('https://web.whatsapp.com/')

    try:
        time.sleep(10)
        input_box = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]'))
        )
        input_box.send_keys(phone_number)
        time.sleep(3)

        try:
            profile_picture = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.CLASS_NAME, '_1AHcd'))
            )
            profile_picture.click()
            time.sleep(5)

            try:
                last_seen = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/header/div[2]/div[2]/span'))
                )
                print(f"Last Seen: {last_seen.text}")
            except Exception as e:
                print("No data for last seen")

            finally:
                click = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/header/div[1]/div'))
                )
                click.click()

                name = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.XPATH, '//*[@id="app"]/div/div[2]/div[5]/span/div/span/div/div/section/div[1]/div[2]/div/span/span'))
                )
                print(f"Contact Name: {name.text}")

                try:
                    status = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="app"]/div/div[2]/div[5]/span/div/span/div/div/section/div[2]/span/span'))
                    )
                    print(f"Status/About: {status.text}")
                except Exception as e:
                    print("No data for About")

                finally:
                    profile_picture_large = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="app"]/div/div[2]/div[5]/span/div/span/div/div/section/div[1]/div[1]/div/img'))
                    )
                    profile_picture_large.click()

                    larger_image = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located(
                            (By.XPATH, '//*[@id="app"]/div/span[3]/div/div/div[2]/div/div/div/div/img'))
                    )
                    larger_image.screenshot(f"{name.text}_profile.png")

        except TimeoutException:
            print("No profile photo!")

        except Exception as e:
            print(f"An error occurred while searching for the image: {e}")

    except Exception as e:
        print("An error occurred while trying to open WhatsApp in the browser.")

    finally:
        driver.quit()

# Example Usage:
phone_number_input = "9619850894"
get_contact_info(phone_number_input)
