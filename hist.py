# -*- coding: UTF-8 -*-

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('example.db')
c = conn.cursor()

x = []

for row in c.execute("SELECT turnoutRounded from Stations"):
	# print(row)
	x.append(row[0])

# the histogram of the data
n, bins, patches = plt.hist(x, 100)

plt.show()
