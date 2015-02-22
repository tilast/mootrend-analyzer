import pymongo
import codecs

connection_string = "mongodb://localhost:27017"
connection = pymongo.MongoClient(connection_string)
database = connection.psv_data

psv_items = database.psv_items

csvFile = open('new_tweets.csv', 'r')

def write_line_to_db(line, flag, item):
  penisesParts = line.split(':=>')
  print len(penisesParts)
  if(flag):
    if(len(penisesParts) > 0):
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
  
  if(len(penisesParts) == 3):
    item["city"] = penisesParts[0]
    item["trend"] = penisesParts[1]
    item["tweet"] = penisesParts[2]
    flag = True  


item = {}
flag = False

for line in csvFile:
  write_line_to_db(line, flag, item)