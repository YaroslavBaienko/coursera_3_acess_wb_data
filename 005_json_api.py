# import urllib.request, json
#
# address = input('Enter location: ')
# print('Retrieving', address)
# with urllib.request.urlopen(address) as url:
#     raw = json.loads(url.read().decode())
#
# print('Retrieved', len(str(raw)), 'characters')
# data = raw.get("comments")
#
# num = total = 0
# for i in range(len(data)):
#     tmp = data[i]
#     value = tmp.get("count")
#     num = num + 1
#     total = total + int(value)
# print("Count:",num)
# print("Sum:",total)

import geopy
import geopy.distance
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # print(json.dumps(js, indent=4))

    pid = js['results'][0]['place_id']
    pid1 = js['results'][0]['formatted_address']
    pid2 =js['results'][0]['geometry']['location']['lat']
    pid3 = js['results'][0]['geometry']['location']['lng']
    print('Place id ', pid)
    print('Adress: ', pid1)
    print('Latitude: ', pid2)
    print('Longitude: ', pid3)