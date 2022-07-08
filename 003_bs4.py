import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# url = input('Enter link: ')
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))

# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter link: ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))


# html = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1588818.html').read()
# soup = BeautifulSoup(html, 'html.parser')
# tags = soup('span')
# sum = 0
# for tag in tags:
#     sum = sum + int(tag.contents[0])
# print(sum)


# url = 'http://python-data.dr-chuck.net/known_by_Conar.html'


url = input('Enter URL:')
count = int(input('Enter count:'))
position = int(input('Enter position:')) - 1
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")
href = soup('a')

for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    soup = BeautifulSoup(html, "html.parser")
    href = soup('a')
