import datetime, re, csv, pprint, requests
import json

# csvfile=open('blogmasteroutput.csv','ab') #this is the excel-compatible file that the data is piped to.
# csvout=csv.writer(csvfile,dialect='excel')

userlist = file('bloglist.txt').readlines()
baseurl =  "https://habitrpg.com/api/v1/user"

for user in userlist:
    try:
        user = user.rstrip()
        print "Checking user->" + str(user) + "<--"
        apikey = raw_input("What is this user's API Key?")
        data = {"x-api-user": user, "x-api-key": apikey}
        print "Compiled user and api key" + str(data)
        print baseurl
        headers = {'content-type': 'application/json'}
        
        r = requests.post(baseurl, data=json.dumps(payload), headers=headers)
        
        print "Response:" + str(r)
    except:
        print "Ack!"
