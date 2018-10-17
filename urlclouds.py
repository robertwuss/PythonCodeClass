
import serial
import time
import astral
import requests




url = 'http://api.openweathermap.org/data/2.5/weather'

citySearch = input()

# print (citySearch)

params = {
   'q': citySearch,
   'APPID': 'f96e96e150fcb459ba5d539d3ec67689'
}

response = requests.get(url, params=params)

data = response.json()

temp = data['main']['temp'] - 272.15
clouds= data['clouds']['all']
# coordlon = data['coord']['lon']
# coordlat = data['coord'] ['lat']



# print('The temp in {} is {}''.format(data['name'],temp))
print ('the temperature in ' + data ['name'] + ' is ' + str(temp))
print ( 'cloud coverage is ' + str(clouds))
# print( str(coordlon))
# print( str(coordlat))

ArduinoSerial = serial.Serial('/dev/cu.usbmodem1411',9600)

time.sleep(2)

if clouds > 10: #if the value is 1
    ArduinoSerial.write(b'0') #send 1
    print ("blue")
    time.sleep(1)
    print ('cloudy')

elif clouds < 10: #if the value is 0
    ArduinoSerial.write(b'1') #send 0
    print ("orange")
    time.sleep(1)
    print ('sunny')

#  if clouds > 50:
#     print ('cloudy')
#
# else:
#      print ('sunny')
