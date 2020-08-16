from bs4 import BeautifulSoup as soup  
from urllib.request import urlopen as uReq  
from tqdm import tqdm
import string
import pandas as pd

pages = ["0-9"]
for i in string.ascii_uppercase:
    pages.append(i.strip())

names = []
short_names = []
fields = []
for i in tqdm(pages):
    page_url = "https://www.asx.com.au/asx/research/listedCompanies.do?coName="+ i
    uClient = uReq(page_url)
    page_soup = soup(uClient.read(), "html.parser")
    containers = page_soup.findAll("td")
    name = []
    for i in range(0,len(containers),3):
        name.append(containers[i].text)
    names.append(name)
    short_name = []
    for i in range(1,len(containers),3):
        short_name.append(containers[i].text)
    short_names.append(short_name)
    field = []
    for i in range(2,len(containers),3):
        field.append(containers[i].text)
    fields.append(field)

names1 = [j for i in names for j in i]
short_names1 = [j for i in short_names for j in i]
fields1 = [j for i in fields for j in i]

company_data = pd.DataFrame([names1,short_names1,fields1]).transpose()
company_data.columns = ['name','short_name','field']
company_data.to_csv("company_data.csv",index = False)




