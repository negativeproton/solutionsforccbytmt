import json
import requests


urlinput='https://cc.the-morpheus.de/challenges/1/'
urloutput='https://cc.the-morpheus.de/solutions/1/'

respsrvr=requests.get(urlinput)
output=respsrvr.text
data={'token':output}
res=requests.post(urloutput, json.dumps(data))

print (res.text)

