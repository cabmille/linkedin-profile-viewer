from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from dotenv import load_dotenv
import os
import time


# Setup WebDriver
driver = webdriver.Chrome()

# Log in to LinkedIn
driver.get('https://www.linkedin.com/login')

# Enter your LinkedIn credentials
username = driver.find_element(By.ID, 'username')
myUsername = os.getenv('LINKEDIN_USERNAME')
username.send_keys(myUsername)  # Enter your username in a cred.venv file

password = driver.find_element(By.ID, 'password')
myPassword = os.getenv('LINKEDIN_PASSWORD')
password.send_keys(myPassword)  # Enter your password in the same cred.venv file
password.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(5)

# Loop through pages 1 to 100
for page in range(1, 101):  # Adjust total_pages as necessary
    driver.get(f'https://www.linkedin.com/search/results/people/?geoUrn=%5B%2290010383%22%5D&keywords=cybersecurity'
               f'&network=%5B%22S%22%5D&origin=FACETED_SEARCH&page={page}&sid=*o0')  # Copy paste your search from
    # LinkedIn and edit the page number with the variable "page" as in this example

    # Wait for the page to load
    time.sleep(3)  # Adjust the sleep time as necessary

    # Locate all profile links on the current page
    profile_links = driver.find_elements(By.XPATH, '//span[contains(@class, "entity-result__title-text")]/a')
    print(f'Page {page} - Number of profiles found: {len(profile_links)}')

    for i in range(len(profile_links)):
        try:
            # Re-locate profile elements in case they have become stale after navigating back
            profile_links = driver.find_elements(By.XPATH, '//span[contains(@class, "entity-result__title-text")]/a')

            # Click on the profile link
            profile_links[i].click()

            # Wait for the profile page to load
            time.sleep(3)  # Adjust sleep as needed for page load

            # Perform any actions on the profile page here
            # e.g., scraping data, interacting with elements, etc.

            # Go back to the original list page
            driver.back()

            # Wait for the list page to reload
            time.sleep(3)  # Adjust sleep as needed for page load

        except StaleElementReferenceException:
            print("Encountered a stale element reference. Skipping to next profile.")
            continue
        except NoSuchElementException as e:
            print(f"Profile element not found: {e}")
            continue
        except Exception as e:
            print(f"Failed to process profile: {e}")
            continue

# Close the WebDriver
driver.quit()