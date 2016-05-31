import requests
import sys
import zipcode

# regiter your api key at:
# https://www.wunderground.com/weather/api/
key = '16-digit wunderground api key'

zc = zipcode.isequal(sys.argv[1])
url = 'http://api.wunderground.com/api/{}/geolookup/conditions/q/{}/{}.json'.format(key, zc.state, sys.argv[1])
r = requests.get(url)

json_string = r.json()
location = json_string['current_observation']['display_location']['full']
temperature = json_string['current_observation']['temperature_string']
feelslike = json_string['current_observation']['feelslike_string']
print('Location: {}'.format(location), sys.argv[1])
print('Temperature: {} \nFeels like:{} '.format(temperature, feelslike))