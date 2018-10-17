import requests

url = 'http://api.openweathermap.org/data/2.5/weather'

# citySearch = input()

# print (citySearch)

params = {
   'q': 'Los Angeles',
   'APPID': 'f96e96e150fcb459ba5d539d3ec67689'
}

response = requests.get(url, params=params)

data = response.json()

temp = data['main']['temp'] - 272.15
clouds= data['clouds']['all']

# print('The temp in {} is {}''.format(data['name'],temp))
print ('the termperature in ' + data ['name'] + ' is ' + str(temp))
print ( 'cloud coverage is ' + str(clouds))


if clouds > 50:
    print ('cloudy')

else: 
     print ('sunny')
