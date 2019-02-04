import json
import requests
import time


urlinput='https://cc.the-morpheus.de/challenges/2/'
urloutput='https://cc.the-morpheus.de/solutions/2/'

def sol2():
    respsrvr=requests.get(urlinput)
    respsrvr=respsrvr.json()
    gesnumber=respsrvr['k']
    geg=respsrvr['list']
    gesindex=geg.index(gesnumber)
    data={'token':gesindex}
    res=requests.post(urloutput, json.dumps(data))
    print(res.text)

    

for i in range(0,6,1):
    sol2()
    time.sleep(1)
