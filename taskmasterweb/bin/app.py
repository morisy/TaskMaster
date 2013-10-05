import web, datetime, re, csv, requests, json

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

members_file = 'members.csv'
members_file = csv.DictReader(open(members_file, 'rb'), delimiter=',', quotechar='"')

#baseurl = "https://habitrpg.com/api/v1/user"


render = web.template.render('templates/')

class Index(object):
    def GET(self):
        members_file = 'members.csv'
        members_file = csv.DictReader(open(members_file, 'rb'), delimiter=',', quotechar='"')
        return render.index(members_file = members_file)

if __name__ == "__main__":
    app.run()
