from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
import feedparser
import urllib2
import BeautifulSoup
import PyRSS2Gen
import datetime
from time import struct_time

from models import Feed, Item

def importFeed(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    
    parsed_feed = feedparser.parse(feed.url)    
    feed_items = []    
    added_count = 0
    for item in parsed_feed["items"]:
        if not Item.objects.filter(guid=item["guid"]):
            item_content = urllib2.urlopen(item["link"]).read()
            soup = BeautifulSoup.BeautifulSoup(item_content)
            body = soup.find(feed.body_element,{"class":feed.body_class})
            feed_item = Item(feed=feed, 
                            title=item["title"], 
                            link=item["link"],
                            guid=item["guid"],
                            pubDate=timestamp_or_now(item),
                            description=unicode(body))
            feed_item.save()
            added_count = added_count + 1
    return HttpResponse("added %d new items OK!" % added_count)

def renderFeed(request, feed_id):
    feed = get_object_or_404(Feed, pk=feed_id)
    items = Item.objects.filter(feed=feed).order_by('-pubDate')
    feed_items = []
    
    for item in items:
        feed_item = PyRSS2Gen.RSSItem(title=item.title, 
                                        link=item.link, 
                                        guid=item.guid,
                                        pubDate=item.pubDate,
                                        description=item.description)
        feed_items.append(feed_item)

    rss = PyRSS2Gen.RSS2(title=feed.title, 
                        link=feed.link, 
                        description=feed.description, 
                        lastBuildDate = datetime.datetime.now(), 
                        items=feed_items)

    return HttpResponse(rss.to_xml())    

def timestamp_or_now(item):
    #pubDate = datetime.datetime(*item["updated_parsed"][:6]),

    date_published = item.get('published_parsed', item.get('updated_parsed'))
    if isinstance(date_published, struct_time):
        date_published = datetime.datetime(*date_published[:-3])
    else:
        date_published = datetime.datetime.utcnow()

    return date_published
