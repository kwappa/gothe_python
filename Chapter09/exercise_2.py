import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://quality-start.in/company/')
soup = BeautifulSoup(req, 'html.parser')
div = soup.find('div', class_ = 'list-group')
for a in div.find_all('a'):
    print(a.string)
