from html.parser import HTMLParser
import urllib.request
# from html.entities import name2codepoint
# import string

class MyHTMLParser(HTMLParser):
    
    def __init__(self):
        super().__init__()
        self.colors = {}
        self.color_name = ""
        self.color_hex = ""
        self.color_in_row = False
    
    def handle_starttag(self, tag, attrs):
        #print("Start tag:", tag)
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href' and attr[1].startswith('/'):
                    self.color_in_row = True
        #if tag == 'a'and self.in_color_row:
            # for attr in attrs:
            #     print(" attr:", attr)
                # if attr[0] == 'href' and attr[1].startswith('/'):
                #     self.color_hex = string('#' + attr[1][1:])
                #     #print("Hex :", attr[1])
                    
    def handle_endtag(self, tag):
        #print("End tag :", tag)
        if tag == 'a':
            self.color_in_row = False
            if self.color_name and self.color_hex:
                self.colors[self.color_name] = self.color_hex
                self.color_name = ""
                self.color_hex = ""
                
    def handle_data(self, data):
        #print("Data :", data)
        if self.color_in_row:
            if data.strip().startswith('#'):
                self.color_hex = data.strip()
            else:
                self.color_name = data.strip()
        
    # def handle_comment(self, data): #This method is called whenever an HTML comment is encountered.
    #     print("Comment :", data)
    # def handle_entityref(self, name): #&lt \ <, &gt \ >, &amp \ &, &quot \ ", &apm \ ' etc.are called entity references.
    #     c = chr(name2codepoint[name])
    #     print("Named ent:", c)
    # def handle_charref(self, name):  #HTML character reference &lt \ < 。#xhhhh; 16進位, #nnnn; 10進位
    #     if name.startswith('x'):
    #         c = chr(int(name[1:], 16))
    #     else:
    #         c = chr(int(name))
    #         print("Num ent :", c)
    # def handle_decl(self, data): #Document Type Declaration (DOCTYPE) is a statement that tells a validator which version of (X)HTML you are using.
    #     print("Decl :", data)
        

# Create an instance of the custom parser
myparser = MyHTMLParser()

# Make an HTTP request and parse the HTML content
with urllib.request.urlopen('https://www.colorhexa.com/color-names') as response:
    html = response.read().decode('utf-8')
    myparser.feed(html)

# Print the extracted data
for color_name, hex_value in myparser.colors.items():
    print(f'{color_name} {hex_value}')

print(f'\nTotal colors: {len(myparser.colors)}')