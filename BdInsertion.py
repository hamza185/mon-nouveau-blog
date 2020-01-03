from sqlite3 import *
import datetime
conn=connect("db.sqlite3")
c=conn.cursor()


#==================================================================insertion dans la table etudiant====================================================================
c.execute("insert into etudiant values(11111,'G154847','Zaizoune','Marouane',datetime('1998-01-12'),'marouane@gmail.com','Big Data et cloud computing','Departement Informatique')")
c.execute("insert into etudiant values(12222,'X399734','Miri','Hamza',datetime('1998-06-21'),'hamza@gmail.com','Big Data et cloud computing','Departement Informatique');")
c.execute("insert into etudiant values(13333,'C124842','Belmzoukia','Amine',datetime('1995-04-24'),'amine@gmail.com','Big Data et cloud computing','Departement Informatique')")
c.execute("insert into etudiant values(14444,'K45265','Matich','Hafsa',datetime('1998-04-15'),'hafsa@gmail.com','Big Data et cloud computing','Departement Informatique')")
c.execute("insert into etudiant values(15555,'RG45212','Rifki','Hanae',datetime('1999-07-14'),'hanae@gmail.com','Big Data et cloud computing','Departement Informatique')")
c.execute("insert into etudiant values(16666,'T124786','Ameziane','Samira',datetime('1998-06-27'),'samira@gmail.com','Big Data et cloud computing','Departement Informatique')")
c.execute("insert into etudiant values(17777,'M666622','Motonne','Zineb',datetime('1998-11-02'),'zineb@gmail.com','Big Data et cloud computing','Departement Informatique')")
c.execute("insert into etudiant values(18888,'P14586','Ahaqyn','Hind',datetime('1998-01-16'),'hind@gmail.com','Big Data et cloud computing','Departement Informatique')")
c.execute("insert into etudiant values(19999,'X54826','Bouhemmou','Hassan',datetime('1998-04-18'),'Hassan@gmail.com','Big Data et cloud computing','Departement Informatique');")

#==================================================================insertion dans la table enseignant====================================================================
c.execute("insert into enseignant values(1111,'Tkatek','Said','said@uit.ac.ma'),(2222,'Abouchabaka','Jaafar','jaafar@uit.ac.ma'),(3333,'Fakhri','Youssef','fakhri@uit.ac.ma'),(4444,'Rafalia','Najat','rafalia@uit.ac.ma'),(5555,'Mourchid','Mohammed','mohammed@uit.ac.ma');")
conn.commit()
conn.close()
