import pandas as pd
from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  
from tqdm import tqdm
import string
import pandas as pd
import multiprocessing as mp
import concurrent.futures
from urllib.request import urlopen, Request
import multiprocessing
import concurrent.futures
from multiprocessing import Pool

data = pd.read_csv("company_data.csv")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"}
def shares(name,return_dict):
    reg_url = "https://www.google.com/search?sxsrf=ALeKk023sZdD6gCxQbbbeoaRnG_0BuxCIQ%3A1597846021699&source=hp&ei=BTI9X9HIKM7y9QOYkLmIBA&q="+name+"+share+price&oq="+name+"+share+price&gs_lcp=CgZwc3ktYWIQAzIMCCMQJxCdAhBGEPoBMgIIADoHCCMQ6gIQJzoHCCMQJxCdAjoECCMQJzoICAAQsQMQkQI6BQgAEJECOgQILhBDOgcILhCxAxBDOgQIABBDOggIABCxAxCDAToLCAAQsQMQgwEQkQI6BwgAELEDEEM6BQgAELEDOgQILhAKOgQIABAKOgYIABAWEB46CAgAEBYQChAeUJjRAliuhQNg2ogDaAJwAHgBgAHcA4gB0RiSAQgwLjE1LjQtMZgBAKABAaoBB2d3cy13aXqwAQo&sclient=psy-ab&ved=0ahUKEwiR35ukuKfrAhVOeX0KHRhIDkEQ4dUDCAk&uact=5"
    req = Request(url=reg_url, headers=headers) 
    uClient = urlopen(req)
    page_soup = soup(uClient.read(), "html.parser")
    share_price = page_soup.find_all('span',{'class':"IsqQVc NprOob XcVN5d"})[0].text
    return_dict[name] = share_price


if __name__ == '__main__':
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    for i in tqdm(list(data.iloc[:10,1])):
        p = multiprocessing.Process(target=shares,args=[i,return_dict])
        jobs.append(p)
        p.start()
    for proc in jobs:
        proc.join()
    print(return_dict)








