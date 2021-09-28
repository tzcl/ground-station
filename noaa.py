#!/usr/bin/env python3

"""Script for recording and decoding NOAA satellite images.

This script performs the following steps:
1. Opens a TCP connection to GQRX
  1. Configures GQRX for the approaching satellite
  2. Tells GQRX to start recording
  3. Tells GQRX to stop recording once the pass finishes
2. Uses SoX to normalise and resample the recorded audio
3. Passes the audio to WXtoIMG to convert to an image
"""

import socket

# Connect to GQRX
# Really, I just need to start the recording and then can drop the connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 7356))  # 7356 is the default port

s.close()
