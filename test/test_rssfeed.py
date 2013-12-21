import unittest
from rsstoevernote import rssfeed

class RSSRequestTest(unittest.TestCase):
    def test_setRssFeed(self):
        r = rssfeed.RssFeed()
        self.assertIsNotNone(r.setRssFeed("http://example.com/"))

    def test_getRssFeedById(self):
        r = rssfeed.RssFeed()
        # Create the required feed for teting
        rsslogid = r.setRssFeed("http://example.com/")
        rsslogId1 = r.getRssFeedById(rsslogid)

        self.assertEqual(rsslogId1[0], rsslogid)
        self.assertEqual(rsslogId1[1], "http://example.com/")

    def test_getAllRssFeed(self):
        r = rssfeed.RssFeed()
        r.setRssFeed("http://example.com/")
        r.setRssFeed("http://example.com/2")
        self.assertGreater(len(r.getAllRssFeed()), 1)

    def test_clearRssFeed(self):
        r = rssfeed.RssFeed()
        r.setRssFeed("http://example.com/")
        r.clearRssFeed()
        self.assertEqual(len(r.getAllRssFeed()), 0)

if __name__ == "__main__":
    unittest.main()