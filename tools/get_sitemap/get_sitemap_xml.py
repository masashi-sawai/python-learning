from bs4 import BeautifulSoup
import requests
import re

path = './urls.txt'
r = requests.get("https://xxxxxx............./sitemap.xml")
c = r.content

bs = BeautifulSoup(c, "html.parser")
# print(bs)
loclist = bs.select("loc")
urls = ''
for loc in loclist:
    urls += re.sub('<[a-z]>', '', loc.text)
    urls += '\n'

with open(path, mode='w') as f:
    f.write(urls)
