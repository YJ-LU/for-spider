from bs4 import BeautifulSoup
import headers
import requests
import random


def req():
    head_list = headers.header_list()
    HEADERS = {'User-Agent': random.choice(head_list)}
    # print(HEADERS)

    url = "https://www.qcc.com/cassets/cb9bfcd31767a81dbef05bd2f6a56ae8.html"
    res = requests.get(url, headers=HEADERS)
    html = res.text

    h1 = BeautifulSoup(html, "html.parser").find_all("h1", class_='copy-value')
    print(h1)
    for t in h1:
        print(t.string)

    # print(html)


if __name__ == "__main__":
    req()
