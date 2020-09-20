import requests
import random
from bs4 import BeautifulSoup
jokes=[]
def say_jokes():
    url="https://www.joydeepdeb.com/misc/one-liners.html"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'lxml')
    for i in range(0,len(soup.find_all('blockquote'))):
        jokes.append(soup.find_all('blockquote')[i].text)
    return jokes[random.randint(0,len(jokes)-1)]

# print(len(jokes)) the length here is 69