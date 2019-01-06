#4sum

import json
import requests
import time

urlc='https://cc.the-morpheus.de/challenges/8/'
urls='https://cc.the-morpheus.de/solutions/8/'

def sol8():
    
    inp=requests.get(urlc)
    inp=inp.json()
    total=inp['k']
    summands=inp['list']
    
    data=solalgo4sum(summands,total)

    output={'token':data}
    res=requests.post(urls,json.dumps(output))

    print(res.text)
    

def solalgo4sum(summands,total):
    for i1 in range(0,(len(summands)-1),1):
        for i2 in range(0,(len(summands)-1),1):
            for i3 in range(0,(len(summands)-1),1):
                for i4 in range(0,(len(summands)-1),1):
                    result=(summands[i1]+summands[i2]+summands[i3]+summands[i4])
                    if result ==total:
                        return [i1,i2,i3,i4]

    
repetition=5

for i in range(0,repetition,1):
    sol8()
    time.sleep(1)
