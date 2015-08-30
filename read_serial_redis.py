from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)


import serial
from hotqueue import HotQueue
from datetime import datetime

ser = serial.Serial('/dev/cu.usbmodem1481', 115200, timeout=1)

queue = HotQueue("serial_message_queue", host="localhost", port=6379, db=0)

#q.put('hello world')

i = 0
#messages = []
message = [datetime.now(),]
number = ''
new_message = False

while True:
    y = ser.read()
    if y == '\r':
        new_message = True
        queue.put(message)
        print(message)
        #messages.append(message)
        message = [datetime.now(),]
    elif y == ' ':
        if number != '':
            message.append(float(number))
        number = ''
    else:
        number = number + y

    i += 1


#print(messages)
ser.close()