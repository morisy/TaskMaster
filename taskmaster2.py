import datetime, re, csv, pprint, requests
import json

# csvfile=open('blogmasteroutput.csv','ab') #this is the excel-compatible file that the data is piped to.
# csvout=csv.writer(csvfile,dialect='excel')


members_file = 'members.csv'
members_file = csv.DictReader(open(members_file, 'rb'), delimiter=',', quotechar='"')


baseurl =  "https://habitrpg.com/api/v1/user"

for user in members_file:
    print "Trying " + str(user['Name']) + "."
    token = user['token']
    apikey = user['key']
    headers = {'content-type': 'application/json', "x-api-user": token, "x-api-key": apikey}
    r = requests.get(baseurl, headers=headers)
    f = open('workfile', 'w')
#   f.write(r.text) 
    tasks = r.json()["tasks"]   
    keys = tasks.keys()        
    todo = []
    for key in keys:
        if tasks[key]["type"] == "todo":
            if not tasks[key]["completed"]:
                print tasks[key]["text"]
                todo.append(tasks[key]["text"])
        f = open('tasks', 'w')
#        f.write(tasks)
