
#Import packages
import requests
import bs4 as bs
import datetime
import json

def beautify(url):
    source = requests.get(url)
    return bs.BeautifulSoup(source.content,"html.parser")

def getProfileDates(i):
	href = i.get('href').split('-')[-3:]
	year,month,day=href[0].encode('ascii'),href[1].encode('ascii'), \
					href[2].encode('ascii')
	return datetime.datetime(year=int(year), month=int(month), day=int(day))

def convertInt(val):

	#Convert string numbers from github into integer values
	try:
		val=int(val.replace(',',''))
	except:
		#if 'k' value, mult by 1000
		if val[-1]=='k':
			val=int(float(val[:-1])*1000)
		#if 'm' value, mult by 1000000
		elif val[-1]=='m':
			val=int(float(val[:-1])*1000000)

	return val

def splitContents(foo):
	return foo.split()

def encodeContents(foo):
	return foo.encode('ascii')

def getContents(foo):
	return splitContents(foo.contents[0])
	#return splitContents(encodeContents(foo.contents[0]))

def getUsersList(numProfile):

	#print '>> Generating list of popular usernames ...'

	#Get list of Users w more than 1000 followers	
	#Extract url from users link
	urls=[]
	for id in range(1,int(numProfile/10+1)):
		url = 'https://github.com/search?o=desc&p='+str(id)+'&q=followers%3A%3E%3D1000&ref=searchresults&s=followers&type=Users'
		soup = beautify(url) 

		for tag in soup.find_all('a'):
			try:	
				if tag.get("class")[0]=='d-table':	
				#if encodeContents(tag.get("class")[0])=='d-table':	
					getItem = tag.get('data-hydro-click')
					#getItem = encodeContents(tag.get('data-hydro-click'))
					jsonItem = json.loads(getItem)
					extractUrl = jsonItem["payload"]["result"]["url"]
					urls.append(extractUrl)

			except:
				pass

	return urls

def getUserStats(currUrl):

	#print '>> Searching ' + currUrl + ' and storing statistics ...'

	#Access user profile and get statistics
	soup = beautify(currUrl) 
	stats=[' ',	\
			0,	\
			0,	\
			0,	\
			0,	\
			0,	\
			datetime.datetime(year=1900, month=1, day=1),	\
			datetime.datetime(year=1900, month=1, day=1),	\
			datetime.datetime(year=1900, month=1, day=1),	\
			datetime.datetime(year=1900, month=1, day=1)	\
			]

	#User profile name
	stats[0] = currUrl.split('/')[-1]
	#stats[0] = encodeContents(currUrl.split('/')[-1])

	#Repos, stars, followers, following
	for tag in soup.find_all('a'):	
		if tag.get('title')=="Repositories":
			for i in tag.find_all('span'):
				stats[1] = convertInt(getContents(i)[0])

		if tag.get('title')=="Stars":
			for i in tag.find_all('span'):
				stats[2] = convertInt(getContents(i)[0])
	
		if tag.get('title')=="Followers":
			for i in tag.find_all('span'):
				stats[3] = convertInt(getContents(i)[0])

		if tag.get('title')=="Following":
			for i in tag.find_all('span'):
				stats[4] = convertInt(getContents(i)[0])

	#Recent contributions and dates for first pull, first issue, first repo, joined
	for tag in soup.find_all('h2'):
		string = getContents(tag)

		if string[1:] == ['contributions', 'in', 'the', 'last', 'year']:
			stats[5]=convertInt(string[0])

		for i in tag.find_all('a'):
			string = getContents(i)
			
			if string == ['First', 'pull', 'request']:
				stats[6] = getProfileDates(i)
			if string == ['First', 'issue']:
				stats[7] = getProfileDates(i)
			if string == ['First', 'repository']:
				stats[8] = getProfileDates(i)
			if string == ['Joined', 'GitHub']:
				stats[9] = getProfileDates(i)

	return stats

def getRepoPages(currUrl):

	repoUrl = currUrl+'?tab=repositories'
	soup = beautify(repoUrl) 

	#####get number of repository pages on single profile
	for tag in soup.find_all('div'):
		try:
			#Look for 'Previous' to define where page numbers are
			indx=[]
			for j in tag.find_all('span'):
				if getContents(j)[0]=='Previous':

					#Make list of all page numbers
					indx=[]
					for i in tag.find_all('a'):
						indx.append(getContents(i)[0])

		except:
			pass

	#Set total number for pages based on prior list
	if len(indx):
		numPg=int(indx[-2])
	else:
		numPg=1

	return numPg

def getProjectsFromRepos(currUrl,numPg):

	#print '>> Searching repository pages and storing repo titles and stats ...'
	
	projects=[]
	#User profile name
	user = currUrl.split('/')[-1]
	#user = encodeContents(currUrl.split('/')[-1])

	for iPg in range(1,numPg+1):
		######Look at all subpages
		subUrl = currUrl+'?page='+str(iPg)+'&tab=repositories'
		soup = beautify(subUrl) 

		#Get recent code repo titles, stars and forks
		flag=0
		for tag in soup.find_all('a'):

			try:
				indx = splitContents(tag.contents[-1])[0]
				#indx = splitContents(encodeContents(tag.contents[-1]))[0]

				#Search for Overview
				if flag==0 and indx =='Overview':
					flag=1

				elif flag==1:
					#Start with repo name
					if tag.get('itemprop')=='name codeRepository':
						repo=[user,getContents(tag)[0],0,0]

					for i in tag.find_all('svg'):
						label=i.get('aria-label')
						#add stars
						if label=='star':
							repo[2]=convertInt(indx)
						#add forks
						elif label=='fork':
							repo[3]=convertInt(indx)
							#append data to projects structure
							projects.append(repo)
							
			except:
				pass

	return projects