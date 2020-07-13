# -*- coding: UTF-8 -*-

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('example.db')
c = conn.cursor()

x = []
y = []
sizes = []

query = '''
SELECT turnoutRounded, Round(Putin*100.0 / (validBallots + invalidBallots)*1.0, 2) as result, Putin from Stations
'''

for row in c.execute(query):
	# print(row)
	x.append(row[0])
	y.append(row[1])
	sizes.append(row[2] / 10000.0)

plt.ylim(0.0, 100.0)
plt.xlim(0.0, 100.0)

fig = plt.figure()
ax = fig.gca()

ax.set_aspect(1)

plt.scatter(x, y, s=sizes)
plt.show()
