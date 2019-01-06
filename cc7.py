import json
import requests
import time

urlc='https://cc.the-morpheus.de/challenges/7/'
urls='https://cc.the-morpheus.de/solutions/7/'

success='Success: TMT{izRWIGQW5BsTv5R0JogU}'
counter=0

def sol7(counter):
    inp=requests.get(urlc)
    inp=inp.json()
    total=inp['k']
    summands=inp['list']
    

    data=indexfinder(summands,total)
    output={'token':data}
    res=requests.post(urls,json.dumps(output))
    
    
    if res.text !=success:
        print("there is a " + res.text)
    print(res.text)

    return counter+1


def indexfinder(summands, total):
    for i in range(0,(len(summands)-1),1):
        ges=total-summands[i]
        if ges in summands:
            index1=i
            index2=summands.index(ges)
            return [index1,index2] 
        
    
repetition=5

for i in range(0,repetition,1):
    counter=sol7(counter)
    time.sleep(0.5)



if counter==repetition:
    print("result: Success!")
