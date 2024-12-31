from scrapper import scrape_and_save_page 
from extract_fields import extract_fields_from_file
import pandas as pd 

def main ():
    timelines = ['now','daily','weekly','monthly','yearly','forever']
    books_data = []
    for timeline in timelines:
        target_url = f"https://openlibrary.org/trending/{timeline}"  # Replace with the URL you want to scrape
        filename = f"{timeline}.txt"

        scrape_and_save_page(target_url,file_name=filename)
        books_data.extend(extract_fields_from_file(filename))

    df = pd.DataFrame(books_data)
       
    df.to_csv("books.csv", index=False)
    print("\nData has been exported to 'books.csv'.")

if __name__=="__main__":
    main()