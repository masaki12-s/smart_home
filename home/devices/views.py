from django.shortcuts import render
from . import models

import os
import sqlite3
from contextlib import closing
from dotenv import load_dotenv
load_dotenv()

db = os.getenv("db")

def devices_template(request):
    print(db)
    # load_device()
    context = {"name" : "test"}# }
    return render(request, 'device.html', context)



