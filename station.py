#!/usr/bin/env python3

import serial
import time
import csv

conn = serial.Serial('usbmodem401', 9600)
time.sleep(2)  # wait for the serial connection to initialise

# passes are stored in rows of timestamp,altitude,azimuth
with open('test.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        conn.write(row['altitude'], row['azimuth'])
        time.sleep(1)

conn.close()
