# charset UTF-8
import sys
import tweepy
import csv
import json
import pymongo
import codecs

consumer_key = "3h3vVfG0sisnB9WBDm4KLLFil"
consumer_secret = "3CHCDaOjefhKDxH5omSfcDcCPE4BABQzgm8Dm2PVlHKtGGuCi2";
access_token = "117166083-oRdQ3CwCIv811BZXkqYIxt11YfJyLXsQ0HrLHuWM"
access_token_secret = "OGxuV3jYrz2bKGaE8OPwhRVQnQV13mjbS08ix1FqE3Xs5"

def write_line_to_db(line, flag, item):
    penisesParts = line.split(':=>')
    print len(penisesParts)
    if (flag):
        if (len(penisesParts) > 0):
            try:
                item["tweet"] = item["tweet"].encode('utf8')
                psv_items.insert(item)
            except Exception, e:
                print "except"
                print e
            item = {}
            flag = False
        else:
            item["tweet"] += " " + line
            flag = True
            return

    if (len(penisesParts) == 3):
        item["city"] = penisesParts[0]
        item["trend"] = penisesParts[1]
        item["tweet"] = penisesParts[2]
        flag = True


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

counter = 0

connection_string = "mongodb://localhost:27017"
connection = pymongo.MongoClient(connection_string)
database = connection.psv_data

psv_items = database.psv_items

item = {}
flag = False

json_result = api.trends_available()
for el in json_result:
    if el[u'countryCode'] == u'US':
        otrends = api.trends_place(el[u'woeid'])
        for trend in otrends[0]['trends']:
            for tweet in tweepy.Cursor(api.search, q=otrends[0][u'trends'][0][u'name'], count=100, \
                                       lang="en", \
                                       since_id=2014 - 06 - 12).items():
                if tweet.text.startswith('RT'):
                    continue

                counter += 1

                if counter > 20:
                    counter = 0
                    break

                try:
                    string = otrends[0][u'locations'][0][u'name'] + ":=>" + trend[u'name'] + ":=>" + tweet.text.encode('utf-8').replace("\n", "")
                    write_line_to_db(string, flag, item)
                except (UnicodeEncodeError, UnicodeDecodeError):
                    print "Caught unicode error"
print counter;