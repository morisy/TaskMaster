import urllib, urllib2, datetime, re, csv, pprint
impor json

# csvfile=open('blogmasteroutput.csv','ab') #this is the excel-compatible file that the data is piped to.
# csvout=csv.writer(csvfile,dialect='excel')

userlist = file('bloglist.txt').readlines()
apikey = raw_input("What is your API Key?")
baseurl =  https://habitrpg.com/api/v1/

for user in userlist:
	try:
		print "Checking user " + str()
		apikey = raw_input("What is this user's API Key?")
		data = {'x-api-user': user, 'x-api-key': apikey}
		req = urllib2.Request(base url + "user", data, {'Content-Type': 'application/json'})
		f = urllib2.urlopen(req)
		response = f.read()
		f.close()
		print response
