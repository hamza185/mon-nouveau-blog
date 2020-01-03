from sqlite3 import *

conn=connect("db.sqlite3")
c=conn.cursor()
res=c.execute("select * ,datetime('now')-date_naiss as age from etudiant")
for ligne in res:
	print(ligne)
conn.close()
