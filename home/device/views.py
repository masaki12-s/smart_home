from django.shortcuts import render
from . import models

import os
import sqlite3
from contextlib import closing
from dotenv import load_dotenv
load_dotenv()

db = os.getenv("db")

def device_template(request):
    load_device()
    context = {"name" : "test"}# }
    return render(request, 'device.html', context)


def load_device():
    with closing(sqlite3.connect(db)) as conn:
        c = conn.cursor()
        
        query = 'SELECT * FROM device'
        c.execute(query)
        resp = {}
        for data in c.fetchall():
            print(data)
        conn.commit()

