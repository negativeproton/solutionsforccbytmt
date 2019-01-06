import json
import requests
import time

repetition=10

urlc='https://cc.the-morpheus.de/challenges/11/' # url challenge 
urls='https://cc.the-morpheus.de/solutions/11/'  # url solution

for i in range(0,repetition,1):
        valid=False
        counter=0   #counts open parentheses
        inp=requests.get(urlc) #input
        inp=inp.text
        
        for i in range(0,len(inp),1):
                if inp[i] is '(' :
                        counter=counter+1
                        
                        if i is (len(inp)-1):
                                valid=False
                                break
                        
                        elif inp[i+1] is ')':
                                valid=False
                                break
                        
                elif inp[i] is ')' :
                        counter=counter-1
                        
                if counter < 0:
                        valid=False
                        break
     
        if counter is 0:
                valid=True




        data={'token':valid}
        res=requests.post(urls,json.dumps(data)) #result server

        #output
        print(inp)
        print('my result: '+str(valid))
        print('result from the server: '+res.text)
        print()

        
        if res.text == 'Error':
                break

        time.sleep(0.5)
