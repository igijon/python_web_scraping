import bs4
import requests

url = 'https://www.filmaffinity.com/es/ranking.php?rn=ranking_scifi'
result = requests.get(url)
print(type(result), result.text)
soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup)
print(soup.select('title'))
print(soup.select('title')[0].getText())
links = soup.select('a')
print(links[0].getText())

movies = soup.select('.movie-card')
print(len(movies))
movies = soup.select('.movie-card .mc-poster a')
for m in movies:
    print(m.attrs['href'])

