# Distance Measurement with Raspberry Pi 4
Measuring different distances to solid and water surfaces with two different distance sensors compatible with a Raspberry Pi 4.

-------------------------------------------------------------------------------------------------------------------------------------

GENERAL USAGE NOTES
-------------------------------------------------------------------------------------------------------------------------------------

- The first script (*sensor_measurement.py*) enables the usage of two distance senors with a Raspberry Pi 4 and saves data in .csv-files.

- The second script (*data_visualisation.py*) visualises the measured values of both sensors per distance for all .csv-files.

- The script was developed as a "Geodata analysis and modelling" seminar work - University of Bern.

- The readme contains the prerequisites one needs to run the code, the set up and contact informations to the developers.

-------------------------------------------------------------------------------------------------------------------------------------

Prerequisites
-------------------------------------------------------------------------------------------------------------------------------------
- Raspberry Pi 4
- Distance sensors:
  * TFMini - Micro LiDAR Module (https://www.sparkfun.com/products/14588?_ga=2.157876282.1489232396.1610894228-276429489.1610894228)
  * Grove - Ultrasonic Ranger (https://wiki.seeedstudio.com/Grove-Ultrasonic_Ranger/)
- Grove Base Hat for Raspberry Pi (optional) (https://www.seeedstudio.com/Grove-Base-Hat-for-Raspberry-Pi.html)
- USB-TTL converter (optional)
- Python Environment (e.g. PyCharm, Geany)
- Packages:
  * serial
  * time
  * csv
  * sys
  * os
  * glob
  * matplotlib
  * pandas

-------------------------------------------------------------------------------------------------------------------------------------

Sensor Setup
-------------------------------------------------------------------------------------------------------------------------------------

TFMini
1) Connect TFmini LiDAR to RPi using USB-TTL converter or UART port using GPIO.
2) If you're using a USB-TTL converter: Check Serial Port, and edit the code accordingly (e.g. ser = serial.Serial('/dev/ttyUSB0',...)


Ultrasonic Ranger
1) Connect Ultrasonic Ranger to RPi using Grove Base Hat for Raspberry Pi or UART port using GPIO.

-------------------------------------------------------------------------------------------------------------------------------------

Scripts
-------------------------------------------------------------------------------------------------------------------------------------

- *sensor_measurement.py*: Script for running both sensors simultainiously and saving data in .csv-file.
- *data_visualisation.py*: Script for visualisimg all created .csv-files automatically.

-------------------------------------------------------------------------------------------------------------------------------------

Execution
-------------------------------------------------------------------------------------------------------------------------------------

For measuring:
1) Open *sensor_measurement.py* script in a Python-Environment
2) Set filename: csvfile = "filename.csv"
3) Run the script

For visualsing the data:
1) Open *data_visualisation.py* script in a Python-Environment
2) Check if .csv-files are in same working directory as *data_visualisation.py*
3) Run the script

-------------------------------------------------------------------------------------------------------------------------------------

Contact
-------------------------------------------------------------------------------------------------------------------------------------
Developers S. Baer, J. Chastonay, D. Reichenbach & E. Siegrist

E-mail: jonas.chastonay@students.unibe.ch

Copyright 2021 University of Bern. All rights reserved.

-------------------------------------------------------------------------------------------------------------------------------------

Acknowledgement
-------------------------------------------------------------------------------------------------------------------------------------
Many thanks to Pascal Horton and Andreas Zischg for the interesting seminar and their support.



