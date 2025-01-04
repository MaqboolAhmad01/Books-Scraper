import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import logging
import os

logger = logging.getLogger(__name__)

# Directory to store pages
BASE_DIR = "Scraped_pages"
# header
HEADERS = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }
    


# Function to scrape a webpage
async def fetch_page(url):
    try:
         # Ensure the directory exists
        if not os.path.exists(BASE_DIR):
            os.makedirs(BASE_DIR)  # Create directory if it doesn't exist
        
        async with aiohttp.ClientSession() as session:
            async with session.get(url=url,headers=HEADERS) as response:
                response.raise_for_status()
                html_content = await response.text()

                # Save the page content to a file
                file_path = os.path.join(BASE_DIR, url.split("/")[-1])
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(html_content)
                    logger.info(f"Page saved to {file_path}")
                    

    except aiohttp.ClientError as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
async def main():
    timelines = ['now','daily','weekly','monthly','yearly','forever']
    
    tasks = [
        fetch_page(f"https://openlibrary.org/trending/{timeline}") for timeline in timelines
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())