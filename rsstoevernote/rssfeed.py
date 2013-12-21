import sqlite3
import os

class RssFeed(object):
    """docstring for RssFeed"""
    def __init__(self):
        super(RssFeed, self).__init__()
        self.conn = sqlite3.connect(os.environ['rsstoevernotedb'])

    def getAllRssFeed(self):
        c = self.conn.cursor()
        return c.execute('SELECT * FROM `rss-feed` ORDER BY id').fetchall()

    def getRssFeedById(self, id):
        c = self.conn.cursor()
        return c.execute('SELECT * FROM `rss-feed` WHERE id=:id', {"id" : id}).fetchone()

    def setRssFeed(self, feedurl):
        c = self.conn.cursor()
        c.execute('INSERT INTO `rss-feed`(`feedurl`) VAlUES (:feedurl)', {"feedurl": feedurl})
        self.conn.commit()
        return c.lastrowid

    def clearRssFeed(self):
        c = self.conn.cursor()
        c.execute('DELETE FROM `rss-feed`')
        self.conn.commit()
