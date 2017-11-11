import serial
ser = serial.Serial("/dev/ttyACM0",230400,timeout=10000)
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

''' humid = float(data[i+2:len(data)])
				print(humid)
			if data[i] == 'r' and data[i+1]== '=':
				pressure = float(data[i+2:len(data)])
				print(pressure)
		j = j+1
		
		ser.close()
	else:
		per = serial.Serial("/dev/ttyS0",230400,timeout=10000)
		for i in range(10):
			data = per.readline()
			print(data)
			for k in range(len(data)):
				if data[k] == '=' and data[k+1] == '-':
					rssi = float(data[i+1:i+4])
					print(rssi)
				elif data[k] == '=' and data[k+1] != '-':
					snr = float(data[i+1:i+2])
					print(snr)
		j = 0
		per.close()



'''
