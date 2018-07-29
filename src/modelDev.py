#Import modules
import sys
import MySQLdb


#Import other scripts
from accessSQL import *
from setupDatabase import *
from loadDatabase import *
from dbClasses import *
from matplotlib.hatch import Stars
from numba.cuda.cudaimpl import lower
from datashape.coretypes import char

def model(numUsers,dbLogin):
	'''
	This is the main function which works to scrape GitHub for important 
	profile and project details

	'''

   
def main(dbLogin):

	#Extract data from database
	db='github_data'
	conn,cur = connectMySQL(dbLogin)
	conn = selectDB(conn,db)
	sql='SELECT '	\
		'repo_projects.repoName,'	\
		'profile_stats.numRepos,'	\
		'profile_stats.numStars,'	\
		'profile_stats.numFollowers,'	\
		'profile_stats.numContributionsLastYear '	\
		'FROM repo_projects '	\
		'INNER JOIN profile_stats '	\
		'ON repo_projects.username = profile_stats.username;'
	#print (sql)
	queryDB(cur,sql)	
	res=cur.fetchall()

	data=[]
	for row in res:
		temp=[None]*6
		
		temp[0]=len(row[0])
		
		if row[0].isalnum():
			temp[1]=1
		else:
			temp[1]=0
		
		temp[2:]=row[1:-1]
		
		data.append(temp)
		print (temp)
	closeDB(conn)
	
	'''
	name--word2vec
	name upp or lower
	name special char
	name repeating
	profile name word2vec
	
	
	label--Stars
	'''
	#Clean and modify data
	#split data

	#Setup model
	#train model
	#test model


if __name__ == "__main__":
	
	#Set script variables
	dbLogin = Credentials('localhost','root','uwO_11njc')
	
	#Call main script
	print ('==============================================')
	print ('           GITHUB SCRAPER NN MODEL            ')
	print ('               v1.0 - 07/2018                 ')
	print ('==============================================')
	print ('>> Running ...')
	main(dbLogin)