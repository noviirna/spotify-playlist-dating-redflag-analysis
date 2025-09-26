import time
import traceback

from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

from .web_api_netlog_processor import process_network_logs
from ..constant.constant import Spotify
from ..helper.validator import validate_url


def get_chromedriver():
    # Create the webdriver object and pass the arguments
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # disable this argument to show the Chrome browser UI
    options.add_argument("--ignore-certificate-errors")
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})

    # Startup the chrome webdriver
    # pass the chrome options as parameters.
    return webdriver.Chrome(options=options)


def scroll_down_element_until_end(driver: webdriver.Chrome, by: str, element_name: str):
    print("scrolling down element")
    try:
        print("begin scroll down")
        (ActionChains(driver)
         .click(driver.find_element(by=by, value=element_name))
         .perform())
        time.sleep(1)
        # note: the scrolling is working visually but the browser won't load the desired API
        # unlike when performing scroll manually
        # next maybe we are going to try to scroll using JS driver !TODO!
        (ActionChains(driver)
         .send_keys(Keys.END)
         .perform())
        time.sleep(1)
    except ElementNotInteractableException:
        # pass through exception can't send keys
        pass
    finally:
        print("finish scroll down")
        time.sleep(30)


def scrape_spotify_playlist_page(playlist_url: str):
    try:
        # Create an empty list variable to put the scraping results
        song_collections = []

        # Validate spotify URL
        if not validate_url(playlist_url):
            print("Invalid URL, can't proceed to continue process")
            return song_collections

        # Set up the Web Driver
        driver = get_chromedriver()

        # Load the page
        print("begin loading page")
        driver.get(playlist_url)
        time.sleep(10)  # to ensure the page is fully loaded, esp when the internet connection is slow
        print("finish loading page")

        # Scroll until recommended track section show to ensure all URL is loaded
        scroll_down_element_until_end(driver,
                                      By.CLASS_NAME,
                                      Spotify.ELEMENT_SELECTED)

        # Filter data from API, this approach chosen because there are no identifier in UI
        song_collections = process_network_logs(driver)
        driver.quit()
        return song_collections
    except Exception:
        traceback.print_exc()
    finally:
        print("end")
