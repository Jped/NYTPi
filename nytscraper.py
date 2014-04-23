#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Acer Customer
#
# Created:     02/03/2014
# Copyright:   (c) Acer Customer 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup
from bs4.diagnose import diagnose
import requests

def get_text(url):
    data=""
    p=requests.get(url).content
    return p
    print type(p)
    soup=BeautifulSoup(p)
    print type(soup)
    print soup
    paragraphs=soup.select("p.story-body-text.story-content")
    data=p
    text=""
    for paragraph in paragraphs:
        text+=paragraph.text
    text=text.encode('ascii', 'ignore')
    return str(text)
print get_text("http://www.nytimes.com/2014/02/23/magazine/instagram-travel-diary.html?nav&_r=0")
