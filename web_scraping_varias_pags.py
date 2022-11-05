import bs4
import requests


def get_books_with_stars():
    page = 1
    url = 'http://books.toscrape.com/catalogue/page-{}.html'
    result = requests.get(url.format(page))
    all_books = []
    while result.ok:
        all_books+=get_books_per_page(result)
        page += 1
        result = requests.get(url.format(page))
    return all_books

def get_books_per_page(result):
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    books = soup.select('.product_pod')
    books_result_page = []
    for b in books:
        if b.select('.star-rating.Four') or b.select('.star-rating.Five'):
            books_result_page.append(b.select('h3 a')[0]['title'])
            print(b.select('h3 a')[0]['title'])

    return books_result_page


print(len(get_books_with_stars()))