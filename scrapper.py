import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape a webpage
def scrape_and_save_page(url, file_name):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive"
        }

        # Send a GET request to the URL
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        nav_bar = soup.find('ul', class_='nav-bar')

        # Extract the <li> elements and their links
        if nav_bar:
            nav_items = nav_bar.find_all('li')  # Find all <li> elements
            extracted_data = []
            for item in nav_items:
                link = item.find('a')  # Find the <a> tag within each <li>
                if link:
                    href = link.get('href')  # Get the href attribute
                    text = link.get_text(strip=True)  # Get the text content
                    extracted_data.append(href)
                    print(f"Text: {text}, Link: {href}")

        # Save the HTML content to a text file
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(soup.prettify())  # Save formatted HTML content
        print(f"Page content successfully saved to '{file_name}'.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Example usage
if __name__ == "__main__":
    slugs = [
        '/trending/now',
        '/trending/daily',
        '/trending/weekly',
        '/trending/monthly',
        '/trending/yearly',
        '/trending/forever',
    ]
    for slug in slugs:
        target_url = f"https://openlibrary.org{slug}"  # Replace with the URL you want to scrape
        scrape_and_save_page(target_url,f"{slug.split("/")[-1]}.txt")
