#!/usr/local/bin/python3

import sqlite3
import dapnet
from geopy.distance import distance

login = 'NOCALL'
passwd = ''
url = 'http://www.hampager.de:8080/calls'

users = ['NOCALL']
txgroup = "oe-oe5"

conn = sqlite3.connect('balloons.db')
c = conn.cursor()
for row in c.execute("SELECT name, latitude, longitude, comment FROM balloons WHERE curtime >= datetime('now', '-5 minutes')"):
	print(row)
	for user in users:
		d = distance((row[1], row[2]), (48.3303333333333, 14.3113333333333)).km
		print(d)
		if d < 10000:
			climb = float(row[3].split()[0].split("=")[1][:-3])
			freq = float(row[3].split()[2])
			text = "%s is in your area! distance: %dkm, climb: %.1fm/s, freq: %.3fMHz" % (row[0], d, climb, freq)
			print(text[:80])
			ret_code = dapnet.send(text[:80], [user], login, passwd, url, txgroup)
			print(ret_code)


conn.close()

