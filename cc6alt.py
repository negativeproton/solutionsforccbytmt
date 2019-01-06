import json
import requests
import time

urlc='https://cc.the-morpheus.de/challenges/6/'
urls='https://cc.the-morpheus.de/solutions/6/'

#own algorithm

def dectobin(dec):
    quo=1
    rest=1
    res=''
    while quo!=0:
        quo=dec//2
        rest=dec%2
        dec=quo
        res=res+str(rest)
    return res[::-1]


repetition=5

for i in range(0,repetition,1):
    inp=requests.get(urlc)
    inp=inp.text
    inp=int(inp)

    inp=dectobin(inp)
    inp=str(inp)
        
    output={'token':inp}
    res=requests.post(urls,json.dumps(output))
    print(res.text)
    time.sleep(0.5)
