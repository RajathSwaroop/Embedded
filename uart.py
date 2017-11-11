import serial
ser = serial.Serial("/dev/ttyS0",115200,timeout=10000)
#per = serial.Serial("/dev/ttyS0",230400,timeout=10000)
#print(ser)
#ser.baudrate = 9600
data = "asdfgh"
temp = 1234.23
humid = 1234.23
pressure = 1234.43
j=0
while True:
	data = ser.readline()
	print(data)	

	per = serial.Serial("/dev/ttyACM0",230400,timeout=10000)
	data = per.readline()
        for k in range(len(data)):
		if data[k] == '=' and data[k+1] == '-':
			rssi = float(data[i+1:i+4])
			print(rssi)
		elif data[k] == '=' and data[k+1] != '-':
			snr = float(data[i+1:i+2])
			print(snr)

per.close()
