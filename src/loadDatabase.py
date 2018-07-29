from accessSQL import *

def loadUsers(cur,conn,urls):

	#print '>>>> Loading users data into database ...'

	#Create sql insert statement
	for i in range(len(urls)):
		user=urls[i].split('/')[-1]

		sql = 'INSERT INTO users ('	\
				'username'	\
				') VALUES ('
		sql += '\'' + str(user) + '\');'

		#Query and commit
		queryDB(cur,sql)
		commitDB(conn)

def loadProfileStats(cur,conn,stats):

	#print '>>>> Loading profile data into database ...'

	#Create sql insert statement
	sql = 'INSERT INTO profile_stats ('	\
			'username,'	\
			'numRepos,'	\
			'numStars,'	\
			'numFollowers,'	\
			'numFollowing,'	\
			'numContributionsLastYear,'	\
			'dateFirstPull,'	\
			'dateFirstIssue,'	\
			'dateFirstRepo,'	\
			'dateJoinGitHub'	\
			') VALUES ('
	for i in range(len(stats)-1):
		sql += '\'' + str(stats[i]) + '\','
	sql += '\'' + str(stats[-1]) + '\');'
	
	#Query and commit
	queryDB(cur,sql)
	commitDB(conn)

def loadRepoProjects(cur,conn,projects):

	#print '>>>> Loading repo projects data into database ...'

	#Go thru all projects
	for j in range(len(projects)):

		#Create sql insert statement
		sql = 'INSERT INTO repo_projects ('	\
				'username,'	\
				'repoName,'	\
				'numStars,'	\
				'numForks'	\
				') VALUES ('
		#Go thru all data values
		for i in range(len(projects[0])-1):
			sql += '\'' + str(projects[j][i]) + '\','
		sql += '\'' + str(projects[j][-1]) + '\');'
		
		#Query and commit
		queryDB(cur,sql)
		commitDB(conn)