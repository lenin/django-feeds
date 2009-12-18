import re
import datetime
import feedparser
from django import template
from django.utils.html import strip_tags

from feeds.models import Feed

register = template.Library()

ddmmyyyy_pattern = re.compile(r'(\d{,2})/(\d{,2})/(\d{4})')
def dateHandler(aDateString):
    """parse a date in DD/MM/YYYY format"""
    day, month, year = ddmmyyyy_pattern.search(aDateString).groups()
    return (int(year), int(month), int(day), 0, 0, 0, 0, 0, 0)
feedparser.registerDateHandler(dateHandler)

def parse_feeds():
    posts = []
    for feed in Feed.active.all():
        feed = feedparser.parse(feed.url)
        for entry in feed['entries'][:5]:
            try:
                pub_date = entry.updated_parsed
                published = datetime.date(pub_date[0], pub_date[1], pub_date[2])
            except:
                published = ''
            try:
                if entry.title == entry.summary:
                    summary = ''
                else:
                    summary = entry.summary
                if summary:
                    summary = strip_tags(summary)
                if not summary and entry.get('content', None):
                    summary = entry.content[0]['value']
            except:
                summary = ''
            posts.append({
                'title': entry.title,
                'summary': summary,
                'link': entry.link,
                'date': published,
            })
    posts = sorted(posts, key=lambda k: k['date'])
    return posts

class ActiveFeedsNode(template.Node):
    def __init__(self, var_name):
        self.var_name = var_name

    def render(self, context):
        context[self.var_name] = parse_feeds()
        return ''

def get_active_feeds(parser, token):
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires arguments" % token.contents.split()[0]
    m = re.search(r'as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError, "%r tag had invalid arguments" % tag_name
    return ActiveFeedsNode(m.groups()[0])
register.tag(get_active_feeds)
