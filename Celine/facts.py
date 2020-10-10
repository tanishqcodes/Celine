from bs4 import BeautifulSoup
import requests
import random
# random.randint() to be used here 
r=requests.get('https://www.thefactsite.com/1000-interesting-facts/')
soup=BeautifulSoup(r.content,'lxml')
# print(len(soup.find_all('p','list')))
# print(len(fact_list))

def tell_facts():
    return soup.find_all('p','list')[random.randint(0,90)].text

