#
# Running and outputting the accelerometer data
# Cheong Chan Oct 2013
#
import calibration
import time

def Accelerometer():
	ser = calibration.getPort()
	for x in range (0,10):
		data = calibration.readArray(ser,32)
		acceleration = calibration.parseDataToXYZ(data)
		print int(acceleration[0][0])
		print int(acceleration[1][0])
		print int(acceleration[2][0])
		time.sleep(.2)	
