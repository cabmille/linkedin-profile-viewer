from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from dotenv import load_dotenv
from pathlib import Path
import os
import time
import re

# Specify the path to your .env file
env_path = Path('/Users/giuliano/PycharmProjects/cybersecScraper/creds.env')
load_dotenv(dotenv_path=env_path)

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
myUsername = os.getenv('USERNAME')
myPassword = os.getenv('PASSWORD')

# Check if environment variables are loaded correctly
if myUsername is None or myPassword is None:
    raise ValueError("Username or password not set in environment variables")

# Setup WebDriver
driver = webdriver.Chrome()

# Log in to LinkedIn
driver.get('https://www.linkedin.com/login')

# Enter your LinkedIn credentials
username = driver.find_element(By.ID, 'username')
username.send_keys(myUsername)  # Enter your username in a cred.venv file

password = driver.find_element(By.ID, 'password')
password.send_keys(myPassword)  # Enter your password in the same cred.venv file
password.send_keys(Keys.RETURN)

# Wait for login to complete
time.sleep(5)

# Change the locations and keywords as you wish
locations = ["Busan"]
keyword = "ceo"

# Regex pattern to extract geoUrn from URL
geoUrn_pattern = re.compile(r'geoUrn=%5B(%22\d+%22)%5D')

for location in locations:  # Loop through locations from the list. Each location contains 100 pages with 1000 profiles

    # Navigate to the search page
    driver.get('https://www.linkedin.com/search/results/people/')

    # Wait for the page to load
    time.sleep(5)
    # Click on the "Locations" filter button

    try:
        locations_button = driver.find_element(By.XPATH, '//button[@id="searchFilter_geoUrn"]')
        locations_button.click()
        time.sleep(2)

    except NoSuchElementException:
        print("Locations button not found. Skipping location.")
        continue

    # Type the location in the search box
    try:
        location_input = driver.find_element(By.XPATH, "//input[@placeholder='Add a location']")
        location_input.send_keys(location)
        time.sleep(3)  # Wait for suggestions to load

        # Press Down Arrow to highlight the first suggestion
        location_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(2)  # Wait for the suggestion to be highlighted

        # Press Enter to select the first suggestion
        location_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the selection to take effect
    except NoSuchElementException:
        print(f"Failed to enter location: {location}. Skipping to next location.")
        continue

    # Click on the "Apply" button to apply the location filter
    try:
        apply_button = driver.find_element(By.XPATH, "//button[@aria-label='Apply current filter to show results']")
        apply_button.click()
        time.sleep(5)  # Wait for the page to reload with the location filter

    except NoSuchElementException:
        print(f"Apply button not found for location: {location}. Skipping to next location.")
        continue

    # Extract the geoUrn from the current URL
    current_url = driver.current_url
    geoUrn_match = geoUrn_pattern.search(current_url)

    if not geoUrn_match:
        print(f"Could not extract geoUrn for location: {location}. Skipping to next location.")
        continue
    geoUrn = geoUrn_match.group(1)

    # Initialize profile counter for this location
    profile_count_total = 0

    # Loop through pages 1 to 100
    for page in range(1, 101):  # Adjust total_pages as necessary

        URL = f'https://www.linkedin.com/search/results/people/?geoUrn=%5B{geoUrn}%5D&&keywords={keyword}&page={page}'
        driver.get(URL)

        # Wait for the page to load
        time.sleep(5)  # Adjust the sleep time as necessary

        # Locate all profile links on the current page
        profile_links = driver.find_elements(By.XPATH, '//span[contains(@class, "entity-result__title-text")]/a')
        print(f'Page {page} - Number of profiles found: {len(profile_links)}')

        for i in range(len(profile_links)):
            try:
                # Re-locate profile elements in case they have become stale after navigating back
                profile_links = driver.find_elements(By.XPATH,
                                                     '//span[contains(@class, "entity-result__title-text")]/a')

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

                # Increment the profile count
                profile_count_total += 1

            except StaleElementReferenceException:
                print("Encountered a stale element reference. Skipping to next profile.")
                continue
            except NoSuchElementException as e:
                print(f"Profile element not found: {e}")
                continue
            except Exception as e:
                print(f"Failed to process profile: {e}")
                continue

    # Print the total number of profiles visited for this location
    print(f'Total profiles visited for {location}: {profile_count_total}')

# Close the WebDriver
driver.quit()