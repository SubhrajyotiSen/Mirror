import urllib2
import json
import html2text

# function to check internet connectivity


def connected(host='http://google.com'):
    try:
        urllib2.urlopen(host)
        return True
    except:
        return False

if connected():
    # base URL for joke
    url = 'http://api.icndb.com/jokes/random'

    # custom header for requests
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'baseURL/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    # setup request using URL and header
    req = urllib2.Request(url, headers=hdr)

    # open the joke page
    page = urllib2.urlopen(req)

    # get the JSON data
    data = json.load(page)

    # check if data is null. Possibly due to access error or website being down
    if data != 'null':

        # extract joke and format it according to HTML tags
        joke = html2text.html2text(data['value']['joke'])
    else:
        joke = 'unable to find a joke'

    # print joke
    print '\n' + joke + '\n'
else:
    print 'No Internet connectivity. PLease check your network and try again'
