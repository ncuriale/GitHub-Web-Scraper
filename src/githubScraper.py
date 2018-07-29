#Import modules
import sys

#Import other scripts
from accessSQL import *
from extractData import *
from setupDatabase import *
from loadDatabase import *
from dbClasses import *

def runScraper(numUsers,dbLogin):
	'''
	This is the main function which works to scrape GitHub for important 
	profile and project details

	'''
	
	#Initial setup of database
	cur,conn = setupDatabase(dbLogin)
				
	#Get list of user profile lists
	urls = getUsersList(numUsers)
	loadUsers(cur,conn,urls)

	#Search through all user profiles
	for currUrl in urls:

		############### Access user main profile #############
		stats = getUserStats(currUrl)
		#Load statistics into database
		loadProfileStats(cur,conn,stats)

		############### Access user repositories ###############
		#get number of repo pages on current profile
		numPg = getRepoPages(currUrl)

		#Search through all repository pages
		projects = getProjectsFromRepos(currUrl,numPg)	
		loadRepoProjects(cur,conn,projects)

	#Close database
	closeDB(conn)

if __name__ == "__main__":
	
	#Set script variables
	numUsers = int(sys.argv[1])
	dbLogin = Credentials('localhost','root',sys.argv[2])
	
	#Call main script
	print ('==============================================')
	print ('               GITHUB SCRAPER                 ')
	print ('               v1.0 - 07/2018                 ')
	print ('==============================================')
	print ('>> Running ...')
	runScraper(numUsers, dbLogin)