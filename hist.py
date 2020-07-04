# -*- coding: UTF-8 -*-

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('example.db')
c = conn.cursor()

x = []

for row in c.execute("SELECT votersInRoll from Stations"):
	# print(row)
	x.append(row[0])

# the histogram of the data
n, bins, patches = plt.hist(x, 5000)


plt.xlabel('No of voters in roll')
plt.ylabel('Probability')
# plt.xlim(0, 8000)
# plt.ylim(0, 1000)
plt.show()
