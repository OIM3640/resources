import csv
import urllib.request
from bs4 import BeautifulSoup


DOWNLOAD_URL = "https://www.imdb.com/chart/top/"


def download_page(url):
    """
    Download the entire page given an URL
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request)


# print(download_page(DOWNLOAD_URL).read())


def parse_html(html):
    """
    Analyze the html page, find the information and return the move list of tuples (movie_name, year)
    """
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    movie_list = soup.find("ul", attrs={"class": "ipc-metadata-list"})
    print(movie_list)
    top_250 = []
    for movie_item in movie_list.find_all("li"):
        summary = movie_item.find(
            "div", attrs={"class": "ipc-metadata-list-summary-item__c"}
        )
        # print(summary)
        # title_link = summary.find("a", attrs={"class": "ipc-title-link-wrapper"})
        # title = title_link.string
        # print(title)
        # metadata = summary.find_all("span", attrs={"class": "cli-title-metadata-item"})
        # year = metadata[0].string
        # print(year)
        # top_250.append((title, year))
    return top_250


# parse_html(download_page(DOWNLOAD_URL).read())


def main():
    url = DOWNLOAD_URL

    # with open("data/imdb_top250.csv", "w", encoding="utf-8", newline="") as f:
    #     writer = csv.writer(f)

    #     fields = ("title", "year")
    #     writer.writerow(fields)

    #     html = download_page(url)
    #     top_250_list = parse_html(html)
    #     writer.writerows(top_250_list)


if __name__ == "__main__":
    main()
