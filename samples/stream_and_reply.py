#author=rhnvrm<hello@rohanverma.net>

from __future__ import absolute_import, print_function

import tweepy
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import key
global api 

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        #this line parses the json data into a python dictionary
        d = json.loads(data)
        
        #uncomment this to explore the dictionary
        print(d , '\n')

        #uncomment this to just see the text of the tweet, simlarly you
        #can see the other fields of the dict
        #print('test: ' + d["text"] + '\n')
        
        #uncomment to to tweet from your twitter bot
        #although before tweeting you might want to implement
        #command parsing and your logic
        #api.update_status(status='[ACMSNUBOT] ' + d["text"])
        

        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(key.consumer_key, key.consumer_secret)
    auth.set_access_token(key.access_token, key.access_token_secret)

    api = tweepy.API(auth)


    stream = Stream(auth, l)
    #change filters to listen to various types of tweets
    #eg try 'coldplay', '@rhnvrm', '#ACMSNU' etc
    stream.filter(track=['#ACMSNU'])
