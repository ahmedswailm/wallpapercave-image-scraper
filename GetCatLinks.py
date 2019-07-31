from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests


geturl = input("Enter your Collection Link :")
html = urlopen(geturl)
bs = BeautifulSoup(html, 'html.parser')
cat_name = geturl.split("/")[-1]
links = bs.findAll("a",{"class":"albumthumbnail"})
catlinks = []
for item in links :
    cat_url = "https://wallpapercave.com"+(item.attrs["href"])
    catlist = catlinks.append("https://wallpapercave.com"+item.get('href'))
    with open(cat_name+ ".txt","a") as outfile  :
        outfile.write(cat_url +"\n")
#        print(cat_url)
print"\n"+ "We will try scraping all Images From The next CateGories :"+"\n")
print(catlinks)
