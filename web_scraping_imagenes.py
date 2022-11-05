import bs4
import requests
import os
from pathlib import Path

url = 'https://www.filmaffinity.com/es/ranking.php?rn=ranking_scifi'
resultado = requests.get(url)
soup = bs4.BeautifulSoup(resultado.text, 'lxml')
imagenes = soup.select('.movie-card .mc-poster img')
for i in imagenes:
    url_file = i['src']
    path_file = url_file.split('/')
    name_file = path_file[len(path_file)-1]
    directory = Path("imagenes")
    if not directory.exists():
        os.mkdir(directory)
    f = open(Path(directory, name_file), 'wb')
    f.write(requests.get(url_file).content)
    f.close()
