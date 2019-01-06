import json
import requests
import time

urlinput='https://cc.the-morpheus.de/challenges/4/'
urloutput='https://cc.the-morpheus.de/solutions/4/'

#rotate a list

def sol4():
    respsrvr=requests.get(urlinput)
    respsrvr=respsrvr.json()
    gegrotate=respsrvr['k']
    gegrotate=int(gegrotate)
    geglist=respsrvr['list']
    newlist=rotate(gegrotate,geglist)
    data={'token':newlist}
    res=requests.post(urloutput, json.dumps(data))
    print(res.text)
    

def rotate(gegrotate,geglist):
    if gegrotate is 0:
        return geglist
    
    for i in range(0,gegrotate,1):
        lastword= geglist[(len(geglist)-1)]
        del geglist[(len(geglist)-1)]
        newlist=[lastword]
        for i in geglist:
            newlist.append(i)
        geglist=newlist

    return geglist

repetition=15

for i in range(0,repetition,1):
    sol4()
    time.sleep(0.5)
