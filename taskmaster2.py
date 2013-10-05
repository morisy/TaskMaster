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

<<<<<<< HEAD
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
=======
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
>>>>>>> e39005b182ac2eefe88832616381dfc9cbe760b7
