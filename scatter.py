# -*- coding: UTF-8 -*-

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect('example.db')
c = conn.cursor()

x = []
y = []
sizes = []

query = '''
SELECT turnout, Putin*1.0 / (validBallots + invalidBallots)*1.0 as result, Putin from Stations
where region not in ("Республика Крым", "Город Севастополь")
'''

for row in c.execute(query):
	# print(row)
	x.append(row[0])
	y.append(row[1])
	sizes.append(float(row[2]) / (70000.0))

# query = '''
# SELECT turnout, Putin*1.0 / (validBallots + invalidBallots)*1.0 as result, votersInRoll from Stations
# where
# 	region = "Чеченская Республика"
# 	AND uik in ("УИК №427", "УИК №386", "УИК №376", "УИК №391", "УИК №438", "УИК №423", "УИК №441", "УИК №443", "УИК №406", "УИК №392")
# '''

# selectionX = []
# selectionY = []
# selectionSizes = []
# for row in c.execute(query):
# 	# print(row)
# 	selectionX.append(row[0])
# 	selectionY.append(row[1])
# 	selectionSizes.append(float(row[2]) / (50.0))


# query = '''
# SELECT turnout, Putin*1.0 / (validBallots + invalidBallots)*1.0 as result, votersInRoll from Stations
# where
# 	region = "Чеченская Республика"
# '''

# selectionX1 = []
# selectionY1 = []
# selectionSizes1 = []
# for row in c.execute(query):
# 	# print(row)
# 	selectionX1.append(row[0])
# 	selectionY1.append(row[1])
# 	selectionSizes1.append(float(row[2]) / (1000.0))

# plt.ylim(0.5, 1.0)
# plt.xlim(0.5, 1.0)

fig = plt.figure()
ax = fig.gca()

ax.set_aspect(1)
plt.scatter(x, y, s=sizes)
# plt.scatter(selectionX, selectionY, s=selectionSizes, marker="x")
# plt.scatter(selectionX1, selectionY1, s=selectionSizes1, c="red")

plt.show()
