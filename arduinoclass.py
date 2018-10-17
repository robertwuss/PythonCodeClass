import serial

port = serial.Serial('/dev/cu.wchusbserial1420')  # open serial port

while True:

    line = port.readline()
    print (line)

    data = line.decode('utf8]')
    print(data)
    print('-')

    stripped_data = data.strip()
    print(stripped_data)

    print ('---')
