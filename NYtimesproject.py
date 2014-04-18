#this is the main file for the program.
#it uses the api link (with my key in it ) to find all of the middle east articles released today
#it takes these linkgs sends them to the helper function and then appends the article and title into a text file
import urllib2 , json, requests, re, os, time
import json
from datetime import date
from bs4 import BeautifulSoup

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
    nytimes_link= "http://api.nytimes.com/svc/search/v2/articlesearch.json?q=middle+east&fq=subsection_name%3A%28%22Middle+East%22%29&begin_date={0}&fl=web_url%2Cheadline&api-key=8eac4eb4e55fbc7fc74d9a6898467d14%3A4%3A68857836".format(todays_date)
    response=urllib2.urlopen(nytimes_link).read()
    print response
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
create_file
print_time="07:40:00"
while True:
    if time.strftime('%X')==print_time:
        create_file()
        time.sleep(60)

