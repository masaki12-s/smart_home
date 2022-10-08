import os
import sqlite3
from contextlib import closing

from dotenv import load_dotenv

load_dotenv()

db = os.getenv("db")

def create_devicedb():
    with closing(sqlite3.connect(db)) as conn:
        c = conn.cursor()
        query = 'CREATE TABLE device(deviceId STRING, deviceName STRING, deviceType STRING, enableCloudService boolean, hubDeviceId STRING)'
        c.execute(query)
        conn.commit()


