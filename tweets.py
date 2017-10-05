import urllib2
from TwitterAPI import TwitterAPI
from keys import *

api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET,
                 ACCESS_TOKEN, ACCESS_SECRET)


def tweetString(string):
    r = api.request('statuses/update', {'status': string})
    print r.status_code


def searchTweets(query):
    r = api.request('search/tweets', {'q': query})
    for item in r:
        print item['user']['screen_name']
        print item['text'] + '\n\n'

print '1. search for tweets '
print '2. tweet something'
ans = input('Enter choice: ')
if ans == 1:
    query = raw_input('Enter term to search for: ')
    searchTweets(query)
elif ans == 2:
    text = raw_input('Enter text to tweet: ')
    tweetString(text)
else:
    print 'Invalid choice'
