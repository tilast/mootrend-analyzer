import pymongo

connection_string = "mongodb://localhost:27017"
connection = pymongo.MongoClient(connection_string)
database = connection.psv_data

psv_items = database.psv_items

