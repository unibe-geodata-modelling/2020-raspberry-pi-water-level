import sys
import time
import csv
from grove.gpio import GPIO
csvfile = "distance_ranger.csv"
usleep = lambda x: time.sleep(x / 1000000.0)

_TIMEOUT1 = 1000
_TIMEOUT2 = 10000

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


def main():
    from grove.helper import SlotHelper
    sh = SlotHelper(SlotHelper.GPIO)
    pin = sh.argv2pin()

    sonar = GroveUltrasonicRanger(pin)

    print('Detecting distance...')
    while True:
        Dist_Total_grove = (sonar.get_distance())
        Dist_Total_grove_int = int(Dist_Total_grove) #Ganzzahlige Distanzmessungen
        #Dist_Total_grove_rounded = round(Dist_Total_grove, 1) #Distanzmessung auf 1 Kommastelle gerundet
        #print (Dist_Total_grove)
        timeGr = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S")
        data_grove = [Dist_Total_grove_int, timeGr]
        print (data_grove)
        #print (round(map(float, Dist_Total_grove)))
        #print('{} cm'.format(sonar.get_distance()))
        time.sleep(1)

        with open(csvfile, "a")as output:
            writer = csv.writer(output, delimiter=",", lineterminator = '\n')
            writer.writerow(data_grove)

if __name__ == '__main__':
    main()

#while(True):
    #Dist_Total_grove = (sonar.get_distance())
    #print (Dist_Total_grove)
      #  timeC = time.strftime("%I")+':' +time.strftime("%M")+':'+time.strftime("%S")
       # data = [Dist_Total, timeC]
      #  print (data)
        
       # with open(csvfile, "a")as output:
             #   writer = csv.writer(output, delimiter=",", lineterminator = '\n')
              #  writer.writerow(data)
       #time.sleep(0.5)
       
       
       #open(csvfile, "a")as output:
        # writer = csv.writer(dist, delimiter=",", lineterminator = '\n')
    #writer.writerow(dist)


