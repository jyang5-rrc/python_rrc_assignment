from html.parser import HTMLParser
import urllib.request
import re

class MyHTMLParser(HTMLParser): 
    def __init__(self,*, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.body = False 
        self.ip = ''

    def handle_starttag(self, tag, attr):
        if tag == 'body':
            self.body = True

    def handle_endtag(self, tag):
        if tag == 'body':
            #print("Found end tag :", tag)
            self.body = False

    def handle_data(self, data):
        if self.body is True:
            #print("Found some data :", data)
            ip_match = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)
            if ip_match is not None:
                self.ip = ip_match.group().strip()

myparser = MyHTMLParser(convert_charrefs=True)
with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
    # html = str(response.read())
    html = response.read().decode('utf-8')
myparser.feed(html)
print(myparser.ip)