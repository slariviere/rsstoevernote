import sqlite3
import os

class RssLog(object):
    """docstring for RssLog"""
    def __init__(self):
        super(RssLog, self).__init__()
        self.conn = sqlite3.connect(os.environ['rsstoevernotedb'])

    def getAllRssLog(self):
        c = self.conn.cursor()
        return c.execute('SELECT * FROM `rss-log` ORDER BY id').fetchall()

    def getRssLogById(self, id):
        c = self.conn.cursor()
        return c.execute('SELECT * FROM `rss-log` WHERE id=:id', {"id" : id}).fetchone()

    def setRssLog(self, idrss, hash):
        c = self.conn.cursor()
        c.execute('INSERT INTO `rss-log`(`id-rss`, hash) VAlUES (?, ?)', (idrss, hash))
        self.conn.commit()
        return c.lastrowid

    def clearRssLog(self):
        c = self.conn.cursor()
        c.execute('DELETE FROM `rss-log`')
        self.conn.commit()
