# -*- coding: UTF-8 -*-

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('example.db')
c = conn.cursor()

x = []
y = []
sizes = []

for row in c.execute("SELECT votersInRoll, Putin*1.0 / (validBallots + invalidBallots)*1.0, turnout from Stations where region = 'город Москва'"):
	# print(row)
	x.append(row[1])
	y.append(row[2])
	sizes.append(float(row[0]) / (7740.0))


plt.ylim(0.0, 1.0)
plt.xlim(0.0, 1.0)
ax = plt.gca()
ax.set_aspect(1)
plt.scatter(x, y, s = sizes)
plt.show()
