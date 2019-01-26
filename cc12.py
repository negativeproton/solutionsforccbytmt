import json
import requests
import time

urlinput='https://cc.the-morpheus.de/challenges/12/'
urloutput='https://cc.the-morpheus.de/solutions/12/'

def sol12():
    respsrvr=requests.get(urlinput)
    respsrvr=respsrvr.json()
    givenlimit=respsrvr['k']
    givenlist=respsrvr['list']

    smallestarraylength=findsmallestarraylength(givenlimit,givenlist)
    data={'token':smallestarraylength}
    res=requests.post(urloutput, json.dumps(data))
    print(res.text)
    print()

    
def findsmallestarraylength(givenlimit,givenlist):
    for i in range(0,len(givenlist),1):
        total=0
        chachearraylength=0
        failed=False
        
        while total<givenlimit:
            #indexerror when values do not get over givenlimit at the end
            if i+chachearraylength == len(givenlist):
                failed=True
                break

            total=total+givenlist[i+chachearraylength]
            chachearraylength=chachearraylength+1

        if failed is True:
            break

        elif i is 0:
            smallestarraylength=chachearraylength

        elif chachearraylength<smallestarraylength:
            smallestarraylength=chachearraylength
    
    return smallestarraylength




repetition=10

for i in range(0,repetition,1):
    print(i)
    sol12()
    time.sleep(0.5)
