import json, requests, re, os, time
import json
from datetime import date
from bs4 import BeautifulSoup
import conf 
"""
this function returns the text of the article from the url
"""
def get_article(url):
    data=""
    html=requests.get(url).content
    match=re.findall(r'<p class="story-body-text story-content".*?</p>', html)
    text=""
    for article in match:
        content=BeautifulSoup(article)
        text+=content.get_text()
    text=text.encode("ascii", "ignore")
    return text

"""
Creates the file by using get article. Prints the File by using print_file
if you run this, it will print out all of the articles
"""
def create_file():
    todays_date=str(date.today())
    todays_date=todays_date.split('-')
    todays_date=todays_date[0]+todays_date[1]+todays_date[2]
    news_file=open(todays_date+".txt", "a")
    nytimes_link= "http://api.nytimes.com/svc/search/v2/articlesearch.json"
    url_parameters={
        "q":"middle east",
        "fq":'subsection_name:("Middle East")',
        "begin_date":todays_date,
        "fl":"web_url,headline",
        "api-key":conf.api_key["api"]
    }
    response=requests.get(nytimes_link, params=url_parameters).text
    response_loaded=json.loads(response)
    for article in response_loaded["response"]["docs"]:
        headline=article["headline"]["main"]
        headline=headline.encode('ascii', 'ignore')
        news_file.write(headline)
        news_file.write("\n \n")
        news_file.write(get_article(article["web_url"]))
        news_file.write("\n \n")
    news_file.close()
    print_file(todays_date)

def print_file(file_name):
    os.system('lpr /home/pi/Desktop/NYT/'+ file_name+".txt")