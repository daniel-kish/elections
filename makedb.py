# -*- coding: UTF-8 -*-

import csv
import sqlite3

rows = []
with open('data/table.txt') as f:
	reader = csv.reader(f, delimiter='\t')
	for row in reader:
		rows.append(row)

colnames = [
	('region', 'text'),
	('tik', 'text'),
	('uik', 'text'),
	('votersInRoll', 'integer'),
	('ballotsAlloted', 'integer'),
	('ballotsIssuedBefore', 'integer'),
	('ballotsIssuedOnStation', 'integer'),
	('ballotsIssuedOutside', 'integer'),
	('ballotsCancelled', 'integer'),
	('ballotsInPortable', 'integer'),
	('ballotsInStationary', 'integer'),
	('invalidBallots', 'integer'),
	('validBallots', 'integer'),
	('lostBallots', 'integer'),
	('unaccountedBallots', 'integer'),
	('Baburin', 'integer'),
	('Grudinin', 'integer'),
	('Zhirinovskiy', 'integer'),
	('Putin', 'integer'),
	('Sobchak', 'integer'),
	('Suraykin', 'integer'),
	('Titov', 'integer'),
	('Yavlinskiy', 'integer'),
	('turnout', 'real'),
	('turnoutRounded', 'real'),
	('url', 'text')
]

# create DB
rowsClause = ""

for x in colnames:
	rowsClause += '`' + x[0].decode('utf-8') + "` {},".format(x[1])

rowsClause = rowsClause[:-1]

createQuery = 'CREATE TABLE IF NOT EXISTS Stations ({})'.decode('utf-8').format(rowsClause)

# print(createQuery)

conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute(createQuery)

for row in rows[1:]:
	region = ("'" + row[0] + "'").decode('utf-8')
	tik = ("'" + row[1] + "'").decode('utf-8')
	uik = ("'" + row[2] + "'").decode('utf-8')
	url = ("'" + row[-1] + "'")
	turnout = (float(row[5]) + float(row[6]) + float(row[7])) / float(row[3])
	turnoutRounded = round(turnout*100.0, 2)

	query = u"INSERT INTO Stations VALUES ({})".format(','.join([region, tik, uik] + row[3:-1] + [turnout.__repr__(), turnoutRounded.__repr__()] + [url]))
	# print(query)
	c.execute(query)

conn.commit()
conn.close()
