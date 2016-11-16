from urllib2 import urlopen
from bs4 import BeautifulSoup
url = 'https://www.wunderground.com/us/va/blacksburg'
raw_data=urlopen(url)
soup=BeautifulSoup(raw_data, 'html.parser')
#print(soup.prettify())
print(soup.find(id="curTemp"))
