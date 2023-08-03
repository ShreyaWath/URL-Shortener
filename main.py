import pyshorteners

url = input('Enter the url : ')

def shorteneurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shorteneurl(url)

