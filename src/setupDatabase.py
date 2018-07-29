from accessSQL import *

def setupDatabase(dbLogin):

	#Connect to MySQL server
	#Use MySQL database credentials
	#print '>> Access and set-up database systems'
	conn, cur = connectMySQL(dbLogin)

	#Refresh and select database -- drop/create database
	db = 'github_data'
	sql = 'DROP DATABASE IF EXISTS ' + db + ';' 
	queryDB(cur,sql)
	sql = 'CREATE DATABASE ' + db 
	queryDB(cur,sql)
	conn = selectDB(conn,db)

	#Creating database tables for future storage
	createUsersTable(cur)
	createProfileTable(cur)
	createProjectTable(cur)

	return cur,conn

def createUsersTable(cur):

	#Create profile stats table
	sql = 'CREATE TABLE users('	\
				'username VARCHAR(255) NOT NULL,'	\
				'PRIMARY KEY(username)'	\
	');'
	queryDB(cur,sql)

def createProfileTable(cur):

	#Create profile stats table
	sql = 'CREATE TABLE profile_stats('	\
				'username VARCHAR(255) NOT NULL,'	\
				'numRepos INT,'	\
				'numStars INT,'	\
				'numFollowers INT,'	\
				'numFollowing INT,'	\
				'numContributionsLastYear INT,'	\
				'dateFirstPull DATETIME,'	\
				'dateFirstIssue DATETIME,'	\
				'dateFirstRepo DATETIME,'	\
				'dateJoinGitHub DATETIME,'	\
				'PRIMARY KEY(username)'	\
	');'
	queryDB(cur,sql)

def createProjectTable(cur):

	#Create repository project table
	sql = 'CREATE TABLE repo_projects('	\
				'username VARCHAR(255) NOT NULL,'	\
				'repoName VARCHAR(255),'	\
				'numStars INT,'	\
				'numForks INT'	\
	');'
	queryDB(cur,sql)

