import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
html = urlopen("http://unseenrajasthan.blogspot.in/")
soup = BeautifulSoup(html,"html.parser")
text = soup.find('body').get_text().strip()
#print(text)
words = text.split()
emails= []
for word in words:
    if re.match(r"[^@]+@[^@]+\.[^@]+",word):
        emails.append(word)
print(emails)
