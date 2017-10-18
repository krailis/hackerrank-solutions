from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for pair in attrs:
            print('-> ' + pair[0] + " > " + str(pair[1]))
    def handle_startendtag(self, tag, attrs):
        print(tag)
        for pair in attrs:
            print('-> ' + pair[0] + " > " + str(pair[1]))

t = int(input())
parser = MyHTMLParser()
snippet = ""
for _ in range(t):
    snippet += input().strip()
parser.feed(''.join(snippet))
