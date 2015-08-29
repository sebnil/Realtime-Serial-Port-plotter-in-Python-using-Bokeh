from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

import redis
import serial
from RedisQueue.RedisQueue import RedisQueue

ser = serial.Serial('/dev/cu.usbmodem1481', 115200, timeout=1)

r = redis.StrictRedis()

r.get("mykey")
q = RedisQueue('y')
#q.put('hello world')

while True:
    y = ser.read()
    r.set('y', y)
    r.set('new_data', True)
    q.put(y)
    print(y)

ser.close()