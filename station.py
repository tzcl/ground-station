#!/usr/bin/env python3

#import serial
import time
import csv
import serial

conn = serial.Serial('/dev/tty.usbmodem401', 9600)

time.sleep(2)  # wait for the serial connection to initialise

# passes are stored in rows of timestamp,altitude,azimuth
with open('test.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msg = row['altitude'] + ' ' + row['azimuth']
        conn.write(msg.encode())
        print(conn.readline().decode('ascii'))
        time.sleep(1)

conn.close()
