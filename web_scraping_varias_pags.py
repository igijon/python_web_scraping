import bs4
import requests


def get_books_with_stars():
    page = 1
    url = 'http://books.toscrape.com/catalogue/page-{}.html'
    result = requests.get(url.format(page))
    while result.ok:
        get_books_per_page(result)
        page += 1
        result = requests.get(url.format(page))

def get_books_per_page(result):
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    books = soup.select('.product_pod')
    for b in books:
        if b.select('.star-rating.Four') or b.select('.star-rating.Five'):
            print(b.select('h3 a')[0]['title'])


get_books_with_stars()