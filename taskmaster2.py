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
        req = requests.put(baseurl, params=data)
        print "Generated request:" + str(req)
        print "Opened page"
        print "Got response"
        print response
    except:
        print "Ack!"
