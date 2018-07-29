# GitHub-Web-Scraper
This module scrapes GitHub profiles for important profile and repository statistics.

The code first populates a list of user with more than 1000 followers. It then uses that list of users to find the following on each profile:
'username,'	
'numRepos,'	
'numStars,'	
'numFollowers,'	
'numFollowing,'	
'numContributionsLastYear,'	
'dateFirstPull,'	
'dateFirstIssue,'	
'dateFirstRepo,'	
'dateJoinGitHub'

The repository pages of each profile are then cycled through and the repository names, stars and forks are extracted. All data is then cleaned/transformed and loaded into a MySQL database.

GitHubScraper can be run with this command:

python githubScraper.py numProfiles databasePassword

