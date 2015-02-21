#!/usr/bin/python

import tweepy

consumer_key = "z8aQINNZfZ0Xp7mFrSpX9enWh"
consumer_secret =  "Lyll5lKv7fJc6QEHhl8C4GOlzaNWTIMUxxQ7tP8JrMr58YqHCK";
access_token = "2217598832-GpBunzNmwpW91Urj4aaRmVlO5KEMUeVq9smUGsF"
access_token_secret = "2LCZ76jOK1TsAYGhVFT0VpYiajLLtyCj4B79EVqX6uJLXB"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text

# user = api.get_user('mefimus')

# print user.screen_name
# print user.followers_count

# Snippet shows available locations for Ukraine

counter = 0

json = api.trends_available()
for el in json:
	counter += 1
	if el[u'countryCode'] == u'US':
		for l in el:
			print str(l) + ": " +  str(el[l])
		print "\n\n"


print counter;

# ua_trends = api.trends_place(23424976)

# import json

# print json.dumps(ua_trends, sort_keys=True, indent=4, separators=(',', ': '))

# for el_1 in ua_trends:
# 	el_2 = el_1[u'trends']
# 	for el_3 in el_2:
# 		print str(el_3) + ": " + str(el_2[el_3])
# 		print "\n\n"


# I've passed exam to Stanford


# I've passed exam to Stanford)))