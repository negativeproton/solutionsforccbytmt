import json
import requests
import time


urlc='https://cc.the-morpheus.de/challenges/10/' #url challenge
urls='https://cc.the-morpheus.de/solutions/10/' #url solution

def sol10():
    inp=requests.get(urlc)
    
    inp=inp.text
    
    resp=float(inp)
    
    output={'token':resp}
    res=requests.post(urls,json.dumps(output))
    print(res.text)

    
    if res.text=='Success: TMT{K84m4dvgwKpU8B6nrBeKNfZb}':
        return 1


    return 0


repetition=10
countertotal=0


print('repetition: '+str(repetition))


for i in range(0,repetition,1):
    countertotal=countertotal+sol10()
    time.sleep(0.5)

print()
print('repetition: '+str(repetition))
print('successfully: '+str(countertotal))
