import unittest
from rsstoevernote import rsslog

class RSSRequestTest(unittest.TestCase):
    def test_setRssLog(self):
        r = rsslog.RssLog()
        self.assertIsNotNone(r.setRssLog("http://example.com/","1234567890"))

    def test_getRssLogById(self):
        r = rsslog.RssLog()
        # Create the required log for teting
        rsslogid = r.setRssLog("http://example.com/","1234567890")
        rsslogId1 = r.getRssLogById(rsslogid)

        self.assertEqual(rsslogId1[0], rsslogid)
        self.assertEqual(rsslogId1[1], "http://example.com/")
        self.assertEqual(rsslogId1[2], "1234567890")

    def test_getAllRssLog(self):
        r = rsslog.RssLog()
        r.setRssLog("http://example.com/","1234567890")
        self.assertGreater(len(r.getAllRssLog()), 0)

    def test_clearRssLog(self):
        r = rsslog.RssLog()
        r.setRssLog("http://example.com/","1234567890")
        r.clearRssLog()
        self.assertEqual(len(r.getAllRssLog()), 0)

if __name__ == "__main__":
    unittest.main()