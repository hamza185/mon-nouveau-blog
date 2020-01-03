from sqlite3 import *

conn=connect("db.sqlite3")
c=conn.cursor()

#================table enseignant=======================================
c.execute("create table if not exists enseignant(num_ens TEXT constraint pk_enseignant primary key,nom_ens varchar(20),prenom_ens varchar(30),email_ens varchar(30));")
#================table etudiant=========================================
c.execute("create table if not exists etudiant(cne TEXT constraint pk_etudiant primary key,cin TEXT,nom_etud varchar(20),prenom_etud varchar(30),date_naiss TEXT,email_etud varchar(30),filiere varchar(40),etablissement varchar(40));")
#================table pfe==============================================
c.execute("create table if not exists pfe(cne TEXT constraint fk_etudiant_soutenance references etudiant,num_ens number(10) constraint fk_etudiant_soutenance references enseignant,id_pfe number(10),titre varchar(50),jury_1 varchar(30),jury_2 varchar(30),date_sout date,validation boolean,note varchar(10),constraint pk_soutenance primary key(cne,num_ens,id_pfe));")

conn.close()
