import unittest
from rsstoevernote import rssrequest

class RSSRequestTest(unittest.TestCase):
    def test_getRawRessFeed(self):
        r = rssrequest.RSSRequest("http://lariviere.me/test.html")
        self.assertEquals("test\n", r.getRawRessFeed())

if __name__ == "__main__":
    unittest.main()
