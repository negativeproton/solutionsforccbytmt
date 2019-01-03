import json
import requests
import time

urlinput='https://cc.the-morpheus.de/challenges/5/'
urls='https://cc.the-morpheus.de/solutions/5/'


def sol5():
    respsrvr=requests.get(urlinput)
    respsrvr=respsrvr.text
    listarg=listcontent(respsrvr)
    final=berechnen(listarg)
    final=int(final[0])



    output={'token':final}
    res=requests.post(urls,json.dumps(output))
    print(res.text)


def listcontent(respsrvr):
    cache=[]
    newlist=[]
    for i in range(0,len(respsrvr),1):
        if respsrvr[i]=="1" or respsrvr[i]=="2" or respsrvr[i]=="3" or respsrvr[i]=="4" or respsrvr[i]=="5" or respsrvr[i]=="6" or respsrvr[i]=="7" or respsrvr[i]=="8" or respsrvr[i]=="9" or respsrvr[i]=="0":
            cache.append(respsrvr[i])
        elif respsrvr[i]=="+" or respsrvr[i]=="*" or respsrvr[i]=="/" or respsrvr[i]=="-":
            newlist.append(respsrvr[i])
        elif respsrvr[i]==" ":
            if cache!=[]:
                anfuegen="".join(cache)
                newlist.append(anfuegen)
                cache=[]
            
    return newlist

def berechnen(listarg):
    i=0
    while '+' in listarg or '-' in listarg or '*' in listarg or '/' in listarg:

        if listarg[i]=='+':
            sum1=float(listarg[i-2])
            sum2=float(listarg[i-1])
            summe=sum1+sum2
            del listarg[i]
            del listarg[i-2]
            del listarg[i-2]
            listarg.insert((i-2),summe)
            i=0

        elif listarg[i]=='-':
                sum1=float(listarg[i-2])
                sum2=float(listarg[i-1])
                diff=sum1-sum2
                del listarg[i]
                del listarg[i-2]
                del listarg[i-2]
                listarg.insert((i-2),diff)
                i=0

        elif listarg[i]=='/':
                sum1=float(listarg[i-2])
                sum2=float(listarg[i-1])
                summe=sum1/sum2
                del listarg[i]
                del listarg[i-2]
                del listarg[i-2]
                listarg.insert((i-2),summe)
                i=0

        elif listarg[i]=='*':
                sum1=float(listarg[i-2])
                sum2=float(listarg[i-1])
                summe=sum1*sum2
                del listarg[i]
                del listarg[i-2]
                del listarg[i-2]
                listarg.insert((i-2),summe)
                i=0

        else:
            i=i+1
            

    return listarg




repetition=10

for i in range(0,repetition,1):
    sol5()
    time.sleep(0.5)



















