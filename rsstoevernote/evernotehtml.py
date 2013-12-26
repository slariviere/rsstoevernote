from bs4 import BeautifulSoup

class EvernoteHtml(object):
    """docstring for EvernoteHtml"""

    # Evernote does not allows those elements
    prohibitedelements = ["applet", "base", "basefont", "bgsound", "blink", "body", "button", "dir", "embed", "fieldset", "form", "frame", "frameset", "head", "html", "iframe", "ilayer", "input", "isindex", "label", "layer", "legend", "link", "marquee", "menu", "meta", "noframes", "noscript", "object", "optgroup", "option", "param", "plaintext", "script", "select", "style", "textarea", "xml"]

    # Evernote does not allows those inline elements
    prohibitedinlineelements =  ["class", "id", "name", "style"]

    def __init__(self, html_doc):
        super(EvernoteHtml, self).__init__()
        self.html_doc = html_doc
        self.soup = BeautifulSoup(self.html_doc)
        self.__removeInlineElements()
        self.html_doc = str(self.soup.html)
        self.__removeProhibitedElements()

    def __removeProhibitedElements(self):
        # Delete the prohibited elements
        # Might break format of the original rss item
        for prohibitedelement in self.prohibitedelements:
            self.html_doc = self.html_doc.replace("<" + prohibitedelement + ">", "").replace("</" + prohibitedelement + ">", "")

    def __removeInlineElements(self):
        # Delete the prohibited inline elements
        # Might break format of the original rss item
        for tag in self.soup():
            for attribute in self.prohibitedinlineelements:
                del tag[attribute]
