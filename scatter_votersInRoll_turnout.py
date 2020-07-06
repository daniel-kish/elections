# -*- coding: UTF-8 -*-

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('example.db')
c = conn.cursor()

x = []
y = []
sizes = []

for row in c.execute("SELECT votersInRoll, (ballotsIssuedBefore + ballotsIssuedOnStation + ballotsIssuedOutside) from Stations"):
	# print(row)
	x.append(row[0])
	y.append(row[1])


plt.ylim(0.0, 3500)
plt.xlim(0.0, 3500)
ax = plt.gca()
ax.set_aspect(1)
plt.scatter(x, y, s = 0.01, marker=".")
plt.show()
