# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:55:08 2019

@author: Laura.Fiorentino
"""

import os
from flask import Flask
from datetime import datetime
import time

app = Flask(__name__)

        
@app.route('/')
def epoch_time():
    now = datetime.now()
    epoch_time = time.mktime(now.timetuple())
    return str(epoch_time)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
    