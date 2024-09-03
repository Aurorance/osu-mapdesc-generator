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
        user_url = input("Please enter the osu! user profile URL to scrape (format: https://osu.ppy.sh/users/XXXXXXXXX): ")
        if re.match(r'^https://osu\.ppy\.sh/users/\d+$', user_url):
            return user_url
        else:
            print("Invalid URL format. Please make sure the URL is in the format: https://osu.ppy.sh/users/XXXXXXXXX\n")

def scroll_to_bottom(driver, max_scroll_times=3, pause_time=1):
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    for _ in range(max_scroll_times):
        driver.execute_script("window.scrollBy(0, 2500);")
        time.sleep(pause_time)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            print("Reached the bottom of the page.")
            break
        last_height = new_height

def click_show_more_button_within_container(parent_div):
    try:
        while True:
            # Attempt to find the "Show More" button within the specific container and click it
            show_more_button = WebDriverWait(parent_div, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.show-more-link__label-text"))
            )
            show_more_button.click()
            print("Clicked 'Show More' button.")
            time.sleep(2)  # Wait for additional beatmaps to load
    except:
        print("There are no more 'Show More' buttons.")

def main():
    user_url = get_valid_url()
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get(user_url)
        scroll_to_bottom(driver, max_scroll_times=3, pause_time=1)

        try:
            beatmaps_section = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.js-sortable--page[data-page-id="beatmaps"]'))
            )
        except:
            print("The beatmaps section was not found on this page.")
            return []

        # Find all titles of class 'title--page-extra-small'
        titles = beatmaps_section.find_elements(By.CSS_SELECTOR, 'h3.title.title--page-extra-small')

        if len(titles) < 2:
            print("The expected 'Ranked' section title was not found.")
            return []

        # Get the second title
        second_title = titles[1]

        # Use XPath to find the **immediate** following sibling div with the class 'osu-layout__col-container'
        try:
            parent_div = second_title.find_element(By.XPATH, "following-sibling::div[contains(@class, 'osu-layout__col-container')]")
            
            # Check if this `osu-layout__col-container` is the immediate sibling and not further down
            preceding_sibling = parent_div.find_element(By.XPATH, "preceding-sibling::h3[1]")
            if preceding_sibling != second_title:
                print("The user has no ranked beatmaps.")
                return []

        except:
            print("The expected 'Ranked' section container was not found right under the second title.")
            return []

        # Scroll to the targeted section to ensure the "Show More" button is visible
        driver.execute_script("arguments[0].scrollIntoView(true);", second_title)

        # Click the "Show More" button within the specific container if it exists
        click_show_more_button_within_container(parent_div)

        # Attempt to scrape the links to the beatmapsets within the specific container
        links = parent_div.find_elements(By.CSS_SELECTOR, 'a.beatmapset-panel__cover-container')

        if not links:
            print("No beatmap links found under the 'Ranked' section.")
            return []

        # Extract the href attributes (links) from the elements
        link_list = [link.get_attribute('href') for link in links]

        return link_list

    finally:
        driver.quit()

if __name__ == "__main__":
    links = main()
    if links:
        print("Combined list of links:")
        for link in links:
            print(link)
    else:
        print("No links found.")