import json
import requests
import time

urlc='https://cc.the-morpheus.de/challenges/6/'
urls='https://cc.the-morpheus.de/solutions/6/'



def sol6():
    
    inp=requests.get(urlc)
    inp=inp.text
    inp=int(inp)
    inp=bin(inp)
    inp=str(inp)
    inp=inp[2:len(inp)]
    output={'token':inp}
    res=requests.post(urls,json.dumps(output))
    print(res.text)
    

repetition=5

for i in range(0,repetition,1):
    sol6()
    time.sleep(0.5)
