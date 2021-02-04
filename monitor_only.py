import serial
import time
from datetime import datetime
from datetime import date
import serial.tools.list_ports
import csv
import os.path



usb_connected = 0

def serial_connecting():
	usb = 0
	while(usb<200):
	    	try:
			ports = list(serial.tools.list_ports.comports())
			for p in ports:
				com = p[0].split()
				print com[0]
				usb=200
				global ser
				ser = serial.Serial(com[0], baudrate = 9600, timeout=1)
				print "Serial connected to ", com[0]
			if not ports:
				time.sleep(2)
				print "Port disconnected, trying to reconnect..."
		except:
			print "Port disconnected, trying to reconnect..."

	return usb


while(1):
	if usb_connected != 200:
		usb_connected = serial_connecting()
	try:
		txt = ser.readline().decode()
		if txt != '':
			print txt

			# now = datetime.now()
			# current_time = now.strftime("%X")
			# current_date = date.today()
			# csvname = "log/" + str(current_date) + ".csv"
			# text_split = txt.split()
			# # file_exists = os.path.isfile(csvname)

			# with open(csvname, mode='a') as csv_file:
			# 	fieldnames = ['written_at', 'text1', 'text2', 'text3']
			# 	# if not file_exists:
		    #     #     		writer.writeheader()  # file doesn't exist yet, write a header
			# 	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
			# 	writer.writerow({'written_at': str(current_time), 'text1': text_split[0], 'text2': text_split[1], 'text3': text_split[2]})

	except serial.serialutil.SerialException:
		usb_connected = serial_connecting()
	except:
		print "error reading or parsing.."
	# except Exception as e: 
	# 	print e

	time.sleep(.2)	
