#!/usr/bin/python3

import aprslib
import sqlite3
from datetime import datetime

def callback(packet):
	if 'timestamp' in packet and 'object_name' in packet and 'latitude' in packet and 'longitude' in packet and 'course' in packet and 'speed' in packet and 'altitude' in packet and 'comment' in packet:
		print(datetime.now())
		print("+ %s" % packet)
		conn = sqlite3.connect('balloons.db', timeout=10)
		c = conn.cursor()
		c.execute('CREATE TABLE IF NOT EXISTS balloons (name TEXT PRIMARY KEY, curtime TEXT, latitude REAL, longitude REAL, course INT, speed REAL, altitude REAL, comment TEXT)')
		c.execute("REPLACE INTO balloons VALUES ('%s', datetime(%d, 'unixepoch'), %f, %f, %f, %f, %f, '%s')" % (packet['object_name'].strip(), packet['timestamp'], packet['latitude'], packet['longitude'], packet['course'], packet['speed'], packet['altitude'], packet['comment']))
		conn.commit()
		conn.close()
		print()
	else:
		print(datetime.now())
		print("- %s" % packet)
		print()

AIS = aprslib.IS("NOCALL", "00000", "euro.aprs2.net", 14580)
AIS.set_filter("u/APRARX")
AIS.connect()
AIS.consumer(callback)
