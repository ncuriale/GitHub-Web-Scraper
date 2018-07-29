import MySQLdb
from dbClasses import *

def connectMySQL(dbLogin):
	conn = MySQLdb.connect(host=dbLogin.host,    # your host, usually localhost
                     	user=dbLogin.user,         # your username
                     	passwd=dbLogin.passwd)  # your password

	# you must create a Cursor object. It will let
	# you execute all the queries you need
	cur = conn.cursor()
	return conn,cur

def connectDB(dbLogin,db):
	conn = MySQLdb.connect(host=dbLogin.host,    # your host, usually localhost
                     	user=dbLogin.user,         # your username
                     	passwd=dbLogin.passwd,  # your password
                     	db=db)        # name of the data base

	# you must create a Cursor object. It will let
	# you execute all the queries you need
	cur = conn.cursor()
	return conn,cur

def selectDB(conn,database):
	conn.select_db(database)
	return conn

def queryDB(cur,query):
	# execute query
	cur.execute(query)

def commitDB(conn):
	conn.commit()
	
def closeDB(conn):
	conn.close()