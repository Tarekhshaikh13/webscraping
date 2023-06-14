import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



response = requests.get(URL)

soup = BeautifulSoup(response.text,'html.parser')

titles = soup.select('h3.title')

with open('movies.txt', "w",encoding="utf-8") as file:
    for tilte in reversed(titles):
        file.write(f"{tilte.get_text()}\n")



