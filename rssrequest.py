import httplib
from urlparse import urlparse


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
        self.url = urlparse(url)

        # Get the requested file
        self.httpconn = httplib.HTTPConnection(self.url.netloc, timeout=5)
        self.httpconn.request('GET', self.url.path, headers=self.http_headers)

    def getUrl(self):
        return self.url

    def getUserAgent(self):
        return self.user_agent

    def getHttpHeaders(self):
        return self.http_headers

    def getRawRessFeed(self):
        return self.httpconn.getresponse().read()
