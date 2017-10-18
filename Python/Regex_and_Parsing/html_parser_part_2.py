from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)
        
    def handle_comment(self, data):
        if (len(data.split('\n')) == 1):
            print(">>> Single-line Comment")
        else:
            print(">>> Multi-line Comment")
        if data.strip():
            print(data)
    
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

