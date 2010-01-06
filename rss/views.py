from django.http import HttpResponse
import feedparser
import urllib2
import BeautifulSoup
import PyRSS2Gen
import datetime

from models import Item

def hello(request):
    return HttpResponse("hello")

def importFeed(request,url):
    feed = feedparser.parse(url)    
    feed_items = []    

    for item in feed["items"][0:1]:
        item_content = urllib2.urlopen(item["link"]).read()
        soup = BeautifulSoup.BeautifulSoup(item_content)
        body = soup.find('div',{"class":"articleBody"}, text=True)
        feed_item = PyRSS2Gen.RSSItem(title=item["title"], 
                                        link=item["link"], 
                                        guid=item["guid"], 
                                        pubDate=item["updated"],
                                        description=body)
        feed_items.append(feed_item)
    
    rss = PyRSS2Gen.RSS2(title=feed["channel"]["title"], link=feed["channel"]["link"], description=feed["channel"]["description"], lastBuildDate = datetime.datetime.now(),
                        items= feed_items)
                                
    return HttpResponse(rss.to_string)
    