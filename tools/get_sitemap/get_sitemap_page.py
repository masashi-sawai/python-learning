from bs4 import BeautifulSoup
import requests

r = requests.get("https://xxxxxx............./sitemap.xml")
c = r.content

bs = BeautifulSoup(c, "html.parser")

a_list = bs.select("a")
for a in a_list:
    href = a.attrs['href']
    print(href)
