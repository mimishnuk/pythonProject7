import datetime
from pprint import pprint
import requests
from bs4 import BeautifulSoup as BS

URL = "https://rezka.ag/animation/"


HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"
}

def get_html(url, params=""):
    reg = requests. get(url=url, headers=HEADERS, params=params)
    return reg


def get_data(html):
    soup = BS(html, "html.parser")
    items = soup.find_all('div', class_="b-content__inline_item")
    anime = []
    for item in items:
        info = item.find("div", class_="b-content__inline_item-link").find('div').string.split(", ")
        animee = {
            "title": item.find("div", class_="b-content__inline_item-link").find("a").string,
            "link": item.find('div', class_='b-content__inline_item-link').find('a').get('href'),
            "status": item.find('span', class_='info').string
            if item.find('span', class_='info') is not None else "Полнометражка",
        }
        try:
            animee["year"] = info[0]
            animee["country"] = info[1]
            animee["genre"] = info[2]
        except IndexError:
            animee["year"] = info[0]
            animee["country"] = "Unknow"
            animee["genre"] = info[1]


        anime.append(animee)


    return anime

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        animations = []
        for i in range(1, 2):
            html = get_html(f"{URL}page/{i}/")
            current_page = get_data(html.text)
            animations.extend(current_page)
        return animations
    else:
        raise Exception("Error in parser")


start = datetime.datetime.now()
a = parser()
print(len(a))
pprint(a)

print(datetime.datetime.now() - start)