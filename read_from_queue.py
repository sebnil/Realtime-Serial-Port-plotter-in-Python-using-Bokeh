from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

from RedisQueue.RedisQueue import RedisQueue
q = RedisQueue('test')
a = q.get()
print(a)