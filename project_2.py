#enabling https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(),'html.parser')
names = bs.find_all('span',{'class':'green'})
for name in names:
    print(name.get_text())