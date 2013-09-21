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
        headers = {'content-type': 'application/json', "x-api-user": user, "x-api-key": apikey}
        #tasks = json.dumps(requests.get(baseurl, headers=headers))
        r = requests.get(baseurl, headers=headers)
        f = open('workfile', 'w')
        f.write(r.text) 
       

        
        tasks = r.json()["tasks"]   
        keys = tasks.keys()        
        for key in keys:
            if tasks[key]["type"] == "todo":
                if not tasks[key]["completed"]:
                    print tasks[key]["text"]
        f = open('tasks', 'w')
        f.write(tasks)
    except:
        print "Ack!"
