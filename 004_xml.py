import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

# data = '''<person>
# <name>Chuck</name>
# <phone type="int1">
# +380969436622
# </phone>
# <email hide="yes"/>
# </person>'''
#
# tree = ET.fromstring(data)
# print('Name:', tree.find('name').text)
# print('Attr:', tree.find('email').get('hide'))


url = input('Enter url: ')
print('Retrieving', url)

total = 0
count = 0

uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

for item in lst:
    count = count + 1
    t = item.find('count').text
    total = total + float(t)

print('Count:', count)
print('Sum:', total)
