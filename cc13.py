
import json
import requests
import time

urlc='https://cc.the-morpheus.de/challenges/13/'
urls='https://cc.the-morpheus.de/solutions/13/'
def sol13():
    lstnotsort=[]
    inp=requests.get(urlc)
    inp=inp.json()
    for k in inp["lista"]:
        lstnotsort.append(k)
    for k in inp["listb"]:
        lstnotsort.append(k)
    lstsort=sorted(lstnotsort)
    data={"token":lstsort}
    resp=requests.post(urls,json.dumps(data))
    print(resp.text)
    
    #add an own sort algorithm
        
repetition=10

for i in range(0,repetition,1):
    sol13()
    time.sleep(0.5)
