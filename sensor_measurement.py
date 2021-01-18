import serial
import time
import csv
import sys
import os
from grove.gpio import GPIO
from grove.helper import SlotHelper
print os.getcwd()

#set filename
csvfile = "filename.csv"

#set up Grove Ultrasonic Ranger - see also https://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/
pin = 5

usleep = lambda x: time.sleep(x / 1000000.0)

_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

#set up TFMini
#check serial port and edit code accordingly 
ser = serial.Serial('/dev/ttyUSB0',115200,timeout = 1)

#set up TFMini data output format for specific use - see also https://github.com/TFmini/TFmini README.md chapter 4.3 & 6.2
ser.write(0x42)
ser.write(0x57)
ser.write(0x02)
ser.write(0x00)
ser.write(0x00)
ser.write(0x00)
ser.write(0x01)
ser.write(0x06)


#measurement Grove Ultrasonic Ranger - see also https://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/
class GroveUltrasonicRanger(object):
    def __init__(self, pin):
        self.dio = GPIO(pin)

    def _get_distance(self):
        self.dio.dir(GPIO.OUT)
        self.dio.write(0)
        usleep(2)
        self.dio.write(1)
        usleep(10)
        self.dio.write(0)

        self.dio.dir(GPIO.IN)

        t0 = time.time()
        count = 0
        while count < _TIMEOUT1:
            if self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT1:
            return None

        t1 = time.time()
        count = 0
        while count < _TIMEOUT2:
            if not self.dio.read():
                break
            count += 1
        if count >= _TIMEOUT2:
            return None

        t2 = time.time()

        dt = int((t1 - t0) * 1000000)
        if dt > 530:
            return None

        distance = ((t2 - t1) * 1000000 / 29 / 2)    # cm

        return distance

    def get_distance(self):
        while True:
            dist = self._get_distance()
            if dist:
                return dist

Grove = GroveUltrasonicRanger

sonar = GroveUltrasonicRanger(pin)

#measurement TFMini
while(True):
    start = time.time()
    break_2nd = False
    while(True):
        if break_2nd:
            break 
        while(ser.in_waiting >= 9):
            if(('Y' == ser.read()) and ('Y' == ser.read())):
                Dist_L = ser.read()
                Dist_H = ser.read()
                Dist_Total = (ord(Dist_H) * 256) + (ord(Dist_L))
                for i in range (0,5):
                    ser.read()    

            #data writing for both sensors
            timeC = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S")
            data = [Dist_Total,sonar.get_distance(), timeC]
            end = time.time()
            #write data every 1 second(s)
            if end - start >= 1:
                print("recorded")
                
                # write data in the csv file
                with open(csvfile, "a")as output:
                        writer = csv.writer(output, delimiter=",", lineterminator = '\n')
                        writer.writerow(data)
                break_2nd = True
                break
