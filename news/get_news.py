import requests
from bs4 import BeautifulSoup

def download_news(url):
    r1 = requests.get(url)
    coverpage = r1.content
    soup1 = BeautifulSoup(coverpage, 'html5lib')
    coverpage_news = soup1.find_all('div', class_='articulo-titulo')
    x = coverpage_news[0].find_all('p')