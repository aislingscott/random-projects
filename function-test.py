from bs4 import BeautifulSoup
import requests
import json
import urllib.request
import time
import pdb
import datetime

def getresults(endpt):
    links='https://www.instagram.com/aisling.scott/?__a=1&max_id={0}'.format(endpt)
    r = requests.get(links)
    html = r.text.encode("utf-8")
    script=html.decode("utf-8")
    dictionary= json.loads(script)
    data = dictionary["user"]
    f = open('captions-instagram', 'w')
    photos=list(range(0,12))
    for s in photos:
        try:
            print("id: " + data['media']['nodes'][s]['id'], file=f)
            print("caption: "+  data['media']['nodes'][s]['caption'], file=f)
            print("date: " + datetime.datetime.fromtimestamp(int(data['media']['nodes'][s]['date'])).strftime('%Y-%m-%d %H:%M:%S'), file=f)
            print("likes: " + str(data['media']['nodes'][s]['likes']['count']), file=f)
            print("comments: " + str(data['media']['nodes'][s]['comments']['count']), file=f)
        except KeyError:
            print("N/a")
    if data['media']['page_info']['has_next_page']==True:
        print(data['media']['page_info']['end_cursor'])
    else:
        f.close()
end=" "
getresults(end)
