from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)

import time

from celery_app import app

@app.task
def add(x, y):
    time.sleep(3)
    return x + y