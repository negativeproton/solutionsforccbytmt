import json
import requests
import time


urlinput='https://cc.the-morpheus.de/challenges/3/'
urloutput='https://cc.the-morpheus.de/solutions/3/'


def sol3():
    respsrvr=requests.get(urlinput)
    respsrvr=respsrvr.json()
    k=respsrvr['list']
    i=sorted(k)


    gesmax=respsrvr['k']

    gesnumber=i[(len(i)-gesmax)]

    data={'token':gesnumber}
    res=requests.post(urloutput, json.dumps(data))
    print(res.text)


for i in range(0,10,1):
    sol3()
    time.sleep(1)















