#author=rhnvrm<hello@rohanverma.net>

from __future__ import absolute_import, print_function

import tweepy
import json
import key
import requests

import calendar
from datetime import datetime

auth = tweepy.OAuthHandler(key.consumer_key, key.consumer_secret)
auth.set_access_token(key.access_token, key.access_token_secret)

api = tweepy.API(auth)

res = requests.get("https://contesttrackerapi.herokuapp.com/")

#convert to py dict
res = json.loads(res.text)

#uncomment to explore the dictionary
#print(res)

upcoming = res["result"]["upcoming"]

tweet = "Next contest: " + upcoming[0]["StartTime"] + "on " + upcoming[0]["Platform"] +". "+ upcoming[0]["url"]
#print(tweet)

#uncomment to update twitter status
api.update_status(status='[ACMSNUBOT] ' + tweet)

#fill this in to loop over the list
#for i in res["ongoing"]:
    #print(i)




