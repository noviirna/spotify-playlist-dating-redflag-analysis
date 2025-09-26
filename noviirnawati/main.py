# load .env file in /env directory
from dotenv import load_dotenv, find_dotenv

load_dotenv(dotenv_path=find_dotenv('./env/.env', usecwd=False))

import sys
from .helper import validator
from .web_scraper.web_api_scraper import scrape_spotify_playlist_page

from .sdk.integration import ai_analysis

playlist_link = sys.argv[1]

if validator.str_is_empty_or_none(playlist_link):
    print("Playlist link is empty. Please enter a valid playlist link.")
else:
    songs_collection = scrape_spotify_playlist_page(playlist_link)
    ai_analysis(songs_collection, playlist_link)
