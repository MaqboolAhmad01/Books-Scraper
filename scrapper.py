import requests
from bs4 import BeautifulSoup

# Function to scrape a webpage
def scrape_titles(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract titles (update the tag and class based on the target site)
        titles = soup.find_all('h2')  # Example: Change 'h2' to the appropriate tag
        
        # Display the extracted titles
        print(f"Titles found on {url}:\n")
        for i, title in enumerate(titles, start=1):
            print(f"{i}. {title.get_text(strip=True)}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

# Example usage
if __name__ == "__main__":
    target_url = "https://www.barnesandnoble.com/"  # Replace with the URL you want to scrape
    scrape_titles(target_url)
