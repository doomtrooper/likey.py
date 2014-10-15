"""
likey.py
This python script download the top 5 liked photos of FaceBook pages 
USAGE:
    step1: This script requires an access token for working. You can get the FB access token from https://developers.facebook.com/tools/explorer/ .
    step2: Enter the USER NAME of the FB page. Ex: IamSRK, humansofnewyork.

Developed By: Razor, ToothLess.

"""
import http.client
import json
import urllib.parse
import os
import urllib.request


httpser=http.client.HTTPSConnection('graph.facebook.com')

token=input('Please enter your FB access token (https://developers.facebook.com/tools/explorer/) :')


username=input("Enter user name :")

if username!="me":
	httpser.request('GET','/'+username+'?fileds=id&access_token='+token)
	idresp=json.loads(httpser.getresponse().read().decode("utf-8"))["id"]

photype='/uploaded'
try:
	mainreq='/v2.1/'+str(idresp)+'/photos'+photype+'?fields=source,likes.limit(100).summary(true)&limit=100&access_token='+token
	httpser.request('GET',mainreq)
	resp=json.loads(httpser.getresponse().read().decode("utf-8"))
	resp=resp["data"]
except KeyError:
	print(resp)
	exit()

def _getkey(item):
	if "likes" in item:
		item["count"]=item["likes"]["summary"]["total_count"]
	else:
		item["count"]=0
	return item["count"]
resp=sorted(resp,reverse=True,key=_getkey)[:5]

os.system('mkdir '+username)
for j,i in enumerate(resp):
   split=urllib.parse.urlsplit(i["source"])
   filename='./'+username+'/'+str(j+1)+'_'+str(i["count"])+"."+split.path.split(".")[-1]
   urllib.request.urlretrieve(i["source"],filename)
