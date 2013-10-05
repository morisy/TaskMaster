import datetime, re, csv, pprint, requests
import json

members_file = 'members.csv'
members_file = csv.DictReader(open(members_file, 'rb'), delimiter=',', quotechar='"')


baseurl =  "https://habitrpg.com/api/v1/user"

for user in members_file:
    print "Trying " + str(user['Name']) + "."
    token = user['token']
    apikey = user['key']
    headers = {'content-type': 'application/json', "x-api-user": token, "x-api-key": apikey}
    r = requests.get(baseurl, headers=headers)
    tasks = r.json()["tasks"]   
    keys = tasks.keys()        
    for key in keys:
        if tasks[key]["type"] == "todo":
            if not tasks[key]["completed"]:
                print tasks[key]["text"]
