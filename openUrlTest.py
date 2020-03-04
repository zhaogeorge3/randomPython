from bs4 import BeautifulSoup
import urllib.request, base64, urllib.error

request = urllib.request.Request("http://www.reddit.com")
string = '%s:%s' % ('zhaogeorge3','CheezyweezY17')

base64string = base64.standard_b64encode(string.encode('utf-8'))

request.add_header("Authorization", "Basic %s" % base64string.decode('utf-8'))
try:
    u = urllib.request.urlopen(request)
except urllib.error.HTTPError as e:
    print(e)
    print(e.headers)

soup = BeautifulSoup(u.read(), 'html.parser')

print(soup.prettify())
