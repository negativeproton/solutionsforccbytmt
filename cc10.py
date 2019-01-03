import json
import requests
import time



urlc='https://cc.the-morpheus.de/challenges/10/' #url challenge
urls='https://cc.the-morpheus.de/solutions/10/' #url solution

def sol10(countersuccessfully):
    inp=requests.get(urlc)
    
    inp=inp.text
    
    resp=float(inp)
    
    output={'token':resp}
    res=requests.post(urls,json.dumps(output))
    print(res.text)
    if res.text=='Error':
        print(res.text)

    if res.text=='Success: TMT{K84m4dvgwKpU8B6nrBeKNfZb}':
        countersuccessfully=countersuccessfully+1


    return countersuccessfully


repetition=10
countersuccessfully=0
countertotal=0


print('repetition: '+str(repetition))


for i in range(0,repetition,1):
    countertotal=countertotal+sol10(countersuccessfully)
    time.sleep(0.5)

print()
print('repetition: '+str(repetition))
print('successfully: '+str(countertotal))







    

