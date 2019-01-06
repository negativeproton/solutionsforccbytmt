#2sum closet

import json
import requests
import time

urlc='https://cc.the-morpheus.de/challenges/9/'
urls='https://cc.the-morpheus.de/solutions/9/'

listall=[]
 

def sol9(listall):
    inp=requests.get(urlc)
    inp=inp.json()
    total=inp['k']
    summands=inp['list']
    listall=solalgo9(summands,total,listall)
    filter(listall)
    
def solalgo9(summands,total,listall):
        for i1 in range(0,(len(summands)-1),1):
            for i2 in range(0,(len(summands)-1),1):
                erg=summands[i1]+summands[i2]
                if erg==total:
                    listall.append([i1,i2])    
        return listall


def filter(listall):
    if len(listall) ==2 or len(listall)==1:
        output={'token':listall[0]}
        res=requests.post(urls,json.dumps(output))
        print(res.text)

    else:
        for i in range(0,int((len(listall)/2)),1):
            seeking=[listall[i][1],listall[i][0]]
            if seeking in listall:
                listall.remove(seeking)

        newlist=[]
        for i in range(0,(len(listall)),1):
            distance=(listall[i][1]-listall[i][0])
            newlist.append(distance)

        smallest=min(newlist)
        seekingindex=newlist.index(smallest)

        output={'token':listall[seekingindex]}
        res=requests.post(urls,json.dumps(output))
        print(res.text)
        
repetition=3

for i in range(0,repetition,1):
    sol9(listall)
    listall=[]
    time.sleep(0.5)
