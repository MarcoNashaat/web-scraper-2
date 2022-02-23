#enabling https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(),'html.parser')
for child in bs.find('table',{'id':'giftList'}).children:
    print(child)

for descendant in bs.find('table',{'id':'giftList'}).descendants:
    print(descendant)