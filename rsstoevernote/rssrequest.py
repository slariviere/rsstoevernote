import requests

# Get the requested url
class RSSRequest(object):
    """Fetch the requested RSSFeed"""

    # When Cloudflare asks if we're a bot, this is what we answer
    user_agent = ' '.join(('Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-ca)',
                          'AppleWebKit/537+ (KHTML, like Gecko) Version/5.0',
                          'Safari/537.6+',
                          'Midori/0.4',
                         ))

    http_headers = {
        'User-Agent': user_agent,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cache-Control': 'max-age=0',
        'Accept-Language': 'en-us;q=1.0',
        'Connection': 'Keep-Alive',
    }

    def __init__(self, url):
        super(RSSRequest, self).__init__()
        self.url = url
        self.r = requests.get(self.url, headers=self.http_headers)

    # Get the fetched URL
    def getUrl(self):
        return self.url

    # Get the http status code (4xx etc.)
    def getHttpCode(self):
        return self.r.status_code

    # Get the http reason (Not found)
    def getHttpReason(self):
        return self.r.reason

    # Get the raw http response
    def getRawRessFeed(self):
        return self.r.text
