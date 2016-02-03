
# coding: utf-8

# In[1]:

import tweepy
import forecastio
from time import strftime


# In[3]:

api_key_forecast = ''


# In[7]:

lat,long = 28.4983598,77.5159955


# In[12]:

forecast = forecastio.load_forecast(api_key_forecast, lat, long)


# In[13]:

forecast


# In[ ]:




# In[32]:

weather_right_now = forecast.currently()


# In[33]:

weather_right_now


# In[34]:

weather_right_now.d


# In[35]:

current_temp = weather_right_now.d['temperature']


# In[36]:

current_temp


# In[50]:

#Don't use mine.

consumer_key=''
consumer_secret=''
access_key=''
access_secret=''


# In[47]:

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)


# In[48]:

api = tweepy.API(auth)


# In[64]:

#Stupid, I know.
def icon(temp):
    if temp>24:
        return u"\u2600"
    else:
        return u"\u2601"


# In[72]:

twitter_status


# In[ ]:

#Infinite loop, updates every hour.
while(True):
    current_temp = weather_right_now.d['temperature']
    twitter_status = "(ACM Talk Demo) It is {0} right now and temp is {1}. {2}".format(timenow,current_temp,icon(current_temp))
    timenow=strftime("%d %b %Y %H:%M:%S")
    api.update_status(status=twitter_status)
    time.sleep(3600)

