# importing the requests library
import requests

URL = "http://maps.googleapis.com/maps/api/geocode/json"

#location = "delhi technological university"
location = "Oracle Redwood city"

# defining a params dict for the parameters to be sent to the API
PARAMS = {'address': location}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)


# extracting data in json format
data = r.json()

print("Response", data)
# extracting latitude, longitude and formatted address
# of the first matching location
#latitude = data['results'][0]['geometry']['location']['lat']
#longitude = data['results'][0]['geometry']['location']['lng']
formatted_address = data['results'][0]['formatted_address']

#print(data)
print(formatted_address)
