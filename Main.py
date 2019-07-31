from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from io import BytesIO
from PIL import Image
import requests
import os
import GetCategories

def scrpingimg(geturl):
    html = urlopen(geturl)
    bs = BeautifulSoup(html, 'html.parser')
    dir_name = geturl.split("/")[-1]
    
    if not os.path.isdir(dir_name) :
        os.mkdir(dir_name)
    images = bs.find_all('img', {'src':re.compile('.jpg')})
    for image in images:

        img_url = "https://wallpapercave.com"+image['src']
        album_title =geturl.split("/")[-1]
        title =album_title+"_"+ img_url.split("/")[-1]
        img_obg = requests.get(img_url)
        print("Getting : "+title+ " | From | "+ img_url)

        try:
           img = Image.open(BytesIO(img_obg.content),"r")
           img.save("./"+dir_name+"/" +title ,img.format)   
        except OSError:
            print("bytes not processed !! - can not save the photo")
            
#Getting Categories Linksr
links = GetCaturl.catlinks
for line in links:
    getlink = line.strip()
    scrpingimg(getlink)

