import json

data = json.load(open('weather.json'))

temp = data['main']['temp'] - 272.15

print ('the weather in' + data ['name'] + ' is ' + str(temp))

# print ('the temperature in {} is{} '.format (data['name'], temp))
