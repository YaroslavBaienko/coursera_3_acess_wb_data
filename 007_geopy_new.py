from geopy import GoogleV3

place = input("Enter address: ")

location = GoogleV3(api_key='AIzaSyCl9k2oHhGfRqwpj3Zdog1u_Hzimqgmca8').geocode(place)

print(location.address)
print(location)