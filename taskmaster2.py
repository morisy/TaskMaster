import datetime, re, csv, pprint, requests
import json

# csvfile=open('blogmasteroutput.csv','ab') #this is the excel-compatible file that the data is piped to.
# csvout=csv.writer(csvfile,dialect='excel')

userlist = file('bloglist.txt').readlines()

members_file = 'members.csv'
members_file = csv.DictReader(open(members_file, 'rb'), delimiter=',', quotechar='"')

#for member in members_file:
#    print member['Name']


baseurl =  "https://habitrpg.com/api/v1/user"

for user in members_file:
    print "Trying " + str(user['Name']) + "."
    token = user['token']
    apikey = user['key']
    data = {"x-api-user": token, "x-api-key": apikey}
    print "Compiled user and api key" + str(data)
    print baseurl
    headers = {'content-type': 'application/json', "x-api-user": token, "x-api-key": apikey}
    r = requests.get(baseurl, headers=headers)
    f = open('workfile', 'w')
    f.write(r.text) 
    print "Response:" + r.text
