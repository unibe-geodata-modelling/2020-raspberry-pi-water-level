import serial
import time
import csv
import sys
import os
print os.getcwd() 
csvfile = "distance_tfmini.csv"

ser = serial.Serial('/dev/ttyUSB0',115200,timeout = 1)
ser.write(0x42)
ser.write(0x57)
ser.write(0x02)
ser.write(0x00)
ser.write(0x00)
ser.write(0x00)
ser.write(0x01)
ser.write(0x06)

while(True):
    while(ser.in_waiting >= 9):
        #print ("a")
        if(('Y' == ser.read()) and ('Y' == ser.read())):
            Dist_L = ser.read()
            Dist_H = ser.read()
            Dist_Total = (ord(Dist_H) * 256) + (ord(Dist_L))
            for i in range (0,5):
                ser.read()
       #time.sleep(0.0005)
        timeC = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S")
        data = [Dist_Total, timeC]
        print (data)
        
        with open(csvfile, "a")as output:
                writer = csv.writer(output, delimiter=",", lineterminator = '\n')
                writer.writerow(data)
       #time.sleep(0.5)
