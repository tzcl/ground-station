#!/usr/bin/env python3
import time
import csv
import serial
import signal
import sys

# conn = serial.Serial('/dev/tty.usbmodem301', 9600)
conn = serial.Serial('COM3', 9600)
time.sleep(2)  # wait for the serial connection to initialise


def interrupt_handler(signal, frame):
    """Ensure serial connection is cleaned up."""
    print("Interrupted! Cleaning up script...")
    conn.close()
    sys.exit(0)


signal.signal(signal.SIGINT, interrupt_handler)

# passes are stored in rows of timestamp,altitude,azimuth
with open('test.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msg = 's' + row['altitude'] + ',' + row['azimuth'] + '\n'
        print(f"Sending: {msg}")
        conn.write(msg.encode('ascii'))
        print(f"{conn.readline().decode('ascii')}")

conn.close()
