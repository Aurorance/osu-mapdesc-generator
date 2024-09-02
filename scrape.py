from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

def get_valid_url():
    while True:
        # Ask user link osu profile
        user_url = input("Please enter the osu! user profile URL to scrape (format: https://osu.ppy.sh/users/XXXXXXXXX): ")

        # Make sure valid osu profile link
        if re.match(r'^https://osu\.ppy\.sh/users/\d+$', user_url):
            return user_url
        else:
            print("Invalid URL format. Please make sure the URL is in the format: https://osu.ppy.sh/users/XXXXXXXXX\n")

def main():
    # Get profile
    user_url = get_valid_url()
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(user_url)

        beatmaps_section = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.js-sortable--page[data-page-id="beatmaps"]'))
        )

        time.sleep(1)

        # Beatmap categories
        titles = beatmaps_section.find_elements(By.CSS_SELECTOR, 'h3.title.title--page-extra-small')

        # Only ranked section
        second_title = titles[1]

        parent_div = second_title.find_element(By.XPATH, "./following-sibling::div")

        driver.execute_script("arguments[0].scrollIntoView(true);", second_title)

        # "Show More" button
        try:
            show_more_button = parent_div.find_element(By.CSS_SELECTOR, "span.show-more-link__label-text")
            show_more_button.click()
        except:
            print("'Show More' button not found or failed to load.")

        time.sleep(1)

        # Scrape the links
        links = parent_div.find_elements(By.CSS_SELECTOR, 'a.beatmapset-panel__cover-container')

        # List
        link_list = [link.get_attribute('href') for link in links]

        return link_list

    finally:
        driver.quit()

if __name__ == "__main__":
    links = main()
    if links:
        print("Combined list of links:")
        print(links)