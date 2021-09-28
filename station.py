#!/usr/bin/env python3

import time
import csv
import serial
import signal
import sys

conn = serial.Serial('/dev/tty.usbmodem401', 9600)

time.sleep(2)  # wait for the serial connection to initialise


def interrupt_handler(signal, frame):
    """Ensure serial connection is cleaned up."""
    print("Interrupted! Cleaning up script...")
    conn.close()
    sys.exit(0)


signal.signal(signal.SIGINT, interrupt_handler)

# passes are stored in rows of timestamp,altitude,azimuth
with open('test.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msg = row['altitude'] + ',' + row['azimuth'] + '\n'
        conn.write(msg.encode('utf-8'))
        print(f"Reply: {conn.readline().decode('utf-8')}")
        time.sleep(2)           # delay in seconds between sending alt/az

conn.close()
