import serial
import time

ArduinoSerial = serial.Serial('/dev/cu.usbmodem1421',9600)

time.sleep(2)


ArduinoSerial.write(b'1')

var = input() #get input from user
print ("you entered", var) #print the input for confirmation

if (var == '1'): #if the value is 1
    ArduinoSerial.write(b'1') #send 1
    print ("LED turned ON")
    time.sleep(1)

if (var == '0'): #if the value is 0
    ArduinoSerial.write(b'0') #send 0
    print ("LED turned OFF")
    time.sleep(1)
