import csv
import urllib.request
from bs4 import BeautifulSoup

BASE_URL = "http://books.toscrape.com/"


def fetch_page_content(url):
    """
    Fetch the content of the page given a URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        return response.read().decode("utf-8")


def extract_books(html):
    """
    Parse the HTML page, find the information and return a list of books as tuples (title, price, availability)
    """
    soup = BeautifulSoup(html, features="html.parser")
    booklist = soup.find("ol", attrs={"class": "row"})
    books = []
    for li in booklist.find_all("li"):
        book = li.find("article", attrs={"class": "product_pod"})
        print(book)
        # title = book.h3.a["title"]
        # print(title)
        # price = book.find("p", attrs={"class": "price_color"}).text
        # print(price)

        # Can you find the availability of the book?
        # availability = None
        # books.append((title, price, availability))
    # return books


def save_books_to_csv(books, filename):
    """
    Save the list of books to a CSV file
    """
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        fields = ("title", "price", "availability")
        writer.writerow(fields)
        writer.writerows(books)


def main():
    url = BASE_URL
    html = fetch_page_content(url)
    # print(html)
    books = extract_books(html)
    # print(books)
    # save_books_to_csv(books, "data/books.csv")


if __name__ == "__main__":
    main()
