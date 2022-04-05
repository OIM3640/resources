import csv
import urllib.request
from bs4 import BeautifulSoup


DOWNLOAD_URL = 'https://www.imdb.com/chart/top'


def download_page(url):
    return urllib.request.urlopen(url)


# print(download_page(DOWNLOAD_URL).read())


def parse_html(html):
    """
    Analyze the html page, find the information and return the move list of tuples (movie_name, year)
    """
    soup = BeautifulSoup(html, features="html.parser")
    # print(soup.prettify())
    movie_table = soup.find('tbody', attrs={'class': 'lister-list'})
    # print(movie_table)
    movie_list = []
    for movie_row in movie_table.find_all('tr'):
        movie_detail = movie_row.find('td', attrs={'class': 'titleColumn'})
        # print(movie_detail)
        movie_name = movie_detail.find('a').string
        # print(movie_name)
        year = movie_detail.find('span', attrs={'class': 'secondaryInfo'}).string.strip('()')
        # print(year)
        movie_list.append((movie_name, year))
    return movie_list


# parse_html(download_page(DOWNLOAD_URL).read())


def main():
    url = DOWNLOAD_URL

    # with open('data/imdb_top250.csv', 'w', encoding='utf-8', newline='') as f:
    #     writer = csv.writer(f)

    #     fields = ('name', 'year')
    #     writer.writerow(fields)

    #     html = download_page(url)
    #     movies = parse_html(html)
    #     writer.writerows(movies)


if __name__ == '__main__':
    main()
