from bs4 import BeautifulSoup
import pandas as pd

def extract_fields_from_file(file_name):
    try:
        # Read the HTML content from the file
        with open(file_name, "r", encoding="utf-8") as file:
            html_content = file.read()

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all book items
        book_items = soup.find_all('li', class_='searchResultItem')

        # Extract book details
        books = []
        for book in book_items:
            title = book.find('h3', class_='booktitle').get_text(strip=True)
            author = book.find('span', class_='bookauthor').find('a').get_text(strip=True)

            pub_year = book.find('span', text=lambda x: x and 'First published' in x).get_text(strip=True).replace('First published in ', '')
            cta_buttons = book.find_all('a', class_='cta-btn')
            statuses = [btn.get_text(strip=True) for btn in cta_buttons]
            books.append({
                'Title': title,
                'Author': author,
                'Publication Year': pub_year,
                'Status': statuses
            })
            print(books)
        return books

    except Exception as e:
        print(f"Error processing content: {e}")
        return None
        

if __name__ == "__main__":
  

    # Step 2: Read the saved content and extract specific fields (e.g., all 'h2' tags)
    timelines = ['now.txt','daily.txt','weekly.txt','monthly.txt','yearly.txt','forever.txt']
    books_data=[]
    for file in timelines:
       
        books_data.extend(extract_fields_from_file(file))
    df = pd.DataFrame(books_data)
       
    df.to_csv("books.csv", index=False)
    print("\nData has been exported to 'books.csv'.")