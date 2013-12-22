import feedparser

class Feed(object):
    """docstring for feed"""
    def __init__(self, rawfeed):
        super(Feed, self).__init__()

        # Initiate feed parsing
        self.f = feedparser.parse(rawfeed)

        # Set feed specific properties
        self.title = self.f.feed.title.encode("utf-8")
        self.link = self.f.feed.link.encode("utf-8")
        self.id = self.f.entries[0].id.encode("utf-8")
        self.item_num = len(self.f.entries)

        # Set items properties
        self.publinshed = []
        self.contenttype = []
        self.content = []
        for x in xrange(0,(self.item_num - 1)):
            self.publinshed.append(self.f.entries[x].published.encode("utf-8"))
            self.contenttype.append(self.f.entries[x].content[0].type.encode("utf-8"))
            self.content.append(self.f.entries[x].content[0].value.encode("utf-8"))

