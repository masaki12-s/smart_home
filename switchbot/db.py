import os
import pymysql.cursors

from contextlib import closing

from dotenv import load_dotenv

load_dotenv()

db = os.getenv("db")

def create_devicedb():
    with pymysql.connect(host="localhost", user="root", password="masaki-s" , db = 'smarthome', cursorclass=pymysql.cursors.DictCursor) as db:
        cursor = db.cursor()
        query = 'create table device (deviceId varchar(20), deviceName varchar(20), deviceType varchar(20), hubDeviceId varchar(20));'
        cursor.execute(query)
        db.commit()


def drop_devicedb():
    with pymysql.connect(host="localhost", user="root", password="masaki-s" , db = 'smarthome', cursorclass=pymysql.cursors.DictCursor) as db:
        cursor = db.cursor()
        query = 'DROP TABLE device;'
        cursor.execute(query)
        db.commit()


def update_devicedb(deviceList: dict):
    with pymysql.connect(host="localhost", user="root", password="masaki-s" , db = 'smarthome', cursorclass=pymysql.cursors.DictCursor) as db:
        cursor = db.cursor()
        for device in deviceList:
            deviceId = device["deviceId"]
            deviceName = device["deviceName"]
            deviceType = device["deviceType"]
            ## enableCloudService = device["enableCloudService"] or None
            hubDeviceId = device["hubDeviceId"]
            query = 'INSERT INTO device(deviceid,devicename,deviceType,hubDeviceId) VALUES (%s, %s, %s, %s);'
            cursor.execute(query,(deviceId, deviceName, deviceType, hubDeviceId))
        db.commit()

if __name__ == '__main__':
    db = pymysql.connect(host="localhost", user="root", password="masaki-s" , db = 'smarthome', cursorclass=pymysql.cursors.DictCursor)
    cursor=db.cursor()
    cursor.execute("show tables;")
    db.commit()
    db.close()
    if cursor != None:
        for row in cursor:
            print(row)
    cursor.close()