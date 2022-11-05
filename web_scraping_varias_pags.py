import bs4
import requests

page = 1
url = 'http://books.toscrape.com/catalogue/page-{}.html'

while requests.get(url.format(page)).ok:
    print(url.format(page))
    page += 1

