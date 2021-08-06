import sqlite3
from sqlite3.dbapi2 import connect

#Create necessary connections for the database
connection = sqlite3.connect("project.db") #Name of the database is project.db
cursor = connection.cursor()

#Establish file iterators
fp1 = open("table1.txt","r")
fp2 = open("table2.txt","r")
fp3 = open("table3.txt","r")

#Creation Of Tables
cursor.execute("PRAGMA FOREIGN_KEYS = ON") #Default is OFF to prevent cascading delete effect
connection.commit()
cursor.execute("CREATE TABLE BRANCHES (code TEXT PRIMARY KEY, name TEXT)")
cursor.execute("CREATE TABLE SUBJECTS (code TEXT PRIMARY KEY, name TEXT, credit INTEGER)")
cursor.execute("CREATE TABLE LOOKUP (branchCode TEXT, semester INTEGER, subjectCode TEXT PRIMARY KEY, FOREIGN KEY(branchCode) REFERENCES BRANCHES(code), FOREIGN KEY(subjectCode) REFERENCES SUBJECTS(code))")

#Read Lines from the text files
Lines1 = fp1.readlines()
Lines2 = fp2.readlines()
Lines3 = fp3.readlines()

#Temporary PlaceHolder
tmp = []

for line in Lines1:
    tmp = line.split(',')
    tmp[1] = tmp[1].strip() #Strip Newline character at the end of each line
    print(tmp)
    cursor.execute("insert into BRANCHES (code, name) values (?, ?)",(tmp[0], tmp[1]))
    connection.commit()

for line in Lines3:
    tmp = line.split(',')
    tmp[2] = tmp[2].strip() #Strip Newline character at the end of each line
    print(tmp)
    cursor.execute("insert into SUBJECTS (code, name, credit) values (?, ?, ?)",(tmp[0], tmp[1], int(tmp[2])))
    connection.commit()

for line in Lines2:
    tmp = line.split(',')
    tmp[2] = tmp[2].strip() #Strip Newline character at the end of each line
    print(tmp)
    cursor.execute("insert into LOOKUP (branchCode, semester, subjectCode) values (?, ?, ?)",(tmp[0], int(tmp[1]), tmp[2]))
    connection.commit()

#Display number of changes made to the database
print(connection.total_changes)

#Good practice of closing iterators
fp1.close()
fp2.close()
fp3.close()