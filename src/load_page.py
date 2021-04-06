from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from pathlib import Path
import requests
import config
import sys

from mongo_db import connect_mongo_db
from url_beautifier import prepare_url_for_storage_path

client = connect_mongo_db()
db = client[config.mongo_database]

def get_page_soup(url, allowed_age_in_seconds = config.default_staleness_in_seconds):
    prepared_url = prepare_url_for_storage_path(url)
    page_count = db[config.mongo_collection].count_documents({
        'url': prepared_url,
        'last_downloaded': {
            '$gte': datetime.now() - timedelta(seconds=allowed_age_in_seconds)
        }
    })

    if page_count > 0:
        page_soup = get_file_soup(prepared_url)
        if page_soup is not False:
            return page_soup

    if page_count == 0 or page_soup == False:
        page_soup = download_page_soup(url)
        save_soup_to_file(page_soup, prepared_url)
        update_db(prepared_url)

    return page_soup

def download_page_soup(url):
    response = requests.get(url)
    page_soup = BeautifulSoup(response.content, 'html.parser')
    return page_soup

def update_db(url):
    db[config.mongo_collection].update_one(
        {
            "url": url,
        },
        {
            "$set": {
                "last_downloaded": datetime.now(),
            }
        },
        upsert = True
    )

def save_soup_to_file(page_soup, url):
    create_directory(f'{config.export_path_prefix}/{url}')
    with open(f'{config.export_path_prefix}/{url}', 'w') as f:
        f.write(page_soup.prettify())

def create_directory(path):
    file_name = path.split('/')[-1]
    path = path.replace(file_name, '')
    Path(path).mkdir(parents=True, exist_ok=True)

def get_file_soup(url):
    file_path = f'{config.export_path_prefix}/{url}'
    if Path(file_path).is_file():
        f = open(file_path, "r")
        soup = BeautifulSoup(f.read(), 'html.parser')
        f.close()
        return soup
    return False

if __name__ == "__main__":
    # url = 'https://deepl.com'
    while True:
        url = input("Enter url: ")
        page = get_page_soup(url, 60)
        print(page)