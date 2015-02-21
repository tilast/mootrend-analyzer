import tweepy
import csv
import json

consumer_key = "3h3vVfG0sisnB9WBDm4KLLFil"
consumer_secret =  "3CHCDaOjefhKDxH5omSfcDcCPE4BABQzgm8Dm2PVlHKtGGuCi2";
access_token = "117166083-oRdQ3CwCIv811BZXkqYIxt11YfJyLXsQ0HrLHuWM"
access_token_secret = "OGxuV3jYrz2bKGaE8OPwhRVQnQV13mjbS08ix1FqE3Xs5"

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

# Open/Create a file to append data
csvFile = open('tweets.csv', 'a')
#Use csv Writer
csvWriter = csv.writer(csvFile)

json_result = api.trends_available()
for el in json_result:
  counter += 1
  # if counter > 100:
  #   break
  if el[u'countryCode'] == u'US':
    otrends = api.trends_place(el[u'woeid'])
    # print "<otrend>"
    # print json.dumps(otrends[0]['trends'], sort_keys=True, indent=4, separators=(',', ': '))
    # print "</otrend>"
    # print json.dumps(otrends[0], sort_keys=True, indent=4, separators=(',', ': '))
    for trend in otrends[0]['trends']:
      for tweet in tweepy.Cursor(api.search,q=otrends[0][u'trends'][0][u'name'],count=100,\
                                 lang="en",\
                                 since_id=2014-06-12).items():
        if(tweet.text.startswith('RT')):
          continue
        print tweet.text
        csvWriter.writerow([otrends[0]['locations'][0]['name'], ":=>", trend['name'], ":=>", tweet.text.encode('utf-8')])      

    # for tweet in tweepy.Cursor(api.search,q=otrends[0][u'trends'][0][u'name'],count=100,\
    #                            lang="en",\
    #                            since_id=2014-06-12).items():
    #   print tweet.created_at, tweet.text
    #   csvWriter.writerow([tweet.text.encode('utf-8')])

  # for l in el:
  # 	print str(l) + ": " +  str(el[l])
  # print "\n\n"


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