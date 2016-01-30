#Using Requests Module

#Source:
#https://automatetheboringstuff.com/chapter11/

import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
if(res.status_code == requests.codes.ok):
	#display only first 250 char
	print(res.text[:250])