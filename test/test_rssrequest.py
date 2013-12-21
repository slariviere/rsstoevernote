import unittest
from rsstoevernote import rssrequest

class RSSRequestTest(unittest.TestCase):
    def test_getRawRessFeed(self):
        r = rssrequest.RSSRequest("http://lariviere.me/test.html")
        self.assertEquals("test\n", r.getRawRessFeed())

    def test_CloudflareBlock(self):
        r = rssrequest.RSSRequest("http://www.liquidmatrix.org/blog/")
        self.assertEquals(200, r.getHttpCode())

if __name__ == "__main__":
    unittest.main()
