##################################################
#Calibration function for Analog Accelerometer
#First attempt at something useful in pySerial
#Cheong Chan Oct 15
##################################################
#pySerial wrapper for serial communication
import serial
import serial.tools.list_ports
#import regular expression to parse numbers
import re

#Get the port that has the arduino and accelerometer connected
def getPort():
	port = serial.tools.list_ports.comports()[-1][0]
	ser = serial.Serial(port, 9600, timeout=1)
	return ser

#Get a set of values from the accelerometer in array split by \r\n
def readArray(ser):
	data = ser.read(100)
	splitted = re.split("\r\n+",data)
	return splitted

#Translate the string data to arrays
def parseDataToXYZ(accelerationRawData):
	#Setup acceleration variables
	xAccelerationValues = []
	yAccelerationValues = []
	zAccelerationValues = []
	entries = len(accelerationRawData)
	#Dont use the end entries as they are probably corrupted
	for x in range(1,entries-1):
		print(accelerationRawData[x])
		if re.match('\w\:',accelerationRawData[x]):
			if re.search('\d+',accelerationRawData[x]):
				axis = re.match('\w',accelerationRawData[x]).group(0)
				print(axis)
				if axis == 'X':
					accelerationValue = re.search('\d+',accelerationRawData[x]).group(0)
					xAccelerationValues.append(accelerationValue)
					print(xAccelerationValues)
				elif axis == 'Y':
					accelerationValue = re.search('\d+',accelerationRawData[x]).group(0)
					yAccelerationValues.append(accelerationValue)
					print(yAccelerationValues)
				elif axis == 'Z':
					accelerationValue = re.search('\d+',accelerationRawData[x]).group(0)
					zAccelerationValues.append(accelerationValue)
					print(zAccelerationValues)					
				else:
					print("Did not match any axis!")

def setupAccelerometer():
	ser = getPort()
	data = readArray(ser)
	parseDataToXYZ(data)
