#enabling https
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#importing libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.read(),'html.parser')

for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)

print(bs.find('img',{'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())