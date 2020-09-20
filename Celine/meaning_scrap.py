import requests
from bs4 import BeautifulSoup
# scrapping meanings
def find_meaning(word):
    url =requests.get(f"https://www.dictionary.com/browse/{word}?s=t")
    soup=BeautifulSoup(url.text,'lxml')
    soup_list=soup.find_all("span",class_="one-click-content css-1p89gle e1q3nk1v4")
    return soup_list[0].text

