import os
import sqlite3
from contextlib import closing

from dotenv import load_dotenv

load_dotenv()

db = os.getenv("db")

def create_devicedb():
    with closing(sqlite3.connect(db)) as conn:
        c = conn.cursor()
        query = 'CREATE TABLE device(deviceId STRING, deviceName STRING, deviceType STRING, hubDeviceId STRING)'
        c.execute(query)
        conn.commit()

def drop_devicedb():
    with closing(sqlite3.connect(db)) as conn:
        c = conn.cursor()
        query = 'DROP TABLE device'
        c.execute(query)
        conn.commit()

def update_devicedb(deviceList: dict):
    with closing(sqlite3.connect(db)) as conn:
        c = conn.cursor()
        for device in deviceList:
            deviceId = device["deviceId"]
            deviceName = device["deviceName"]
            deviceType = device["deviceType"]
            ## enableCloudService = device["enableCloudService"] or None
            hubDeviceId = device["hubDeviceId"]
            query = 'INSERT INTO device(deviceid,devicename,deviceType,hubDeviceId) VALUES (?,?,?,?);'
            c.execute(query,[deviceId, deviceName, deviceType, hubDeviceId])
        conn.commit()

if __name__ == '__main__':
    create_devicedb()