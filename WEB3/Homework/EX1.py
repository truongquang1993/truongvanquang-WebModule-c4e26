from pymongo import MongoClient
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

#1. Connect
client = MongoClient(uri)
#2. Data base
db = client.c4e
#3. Close connection
def close():
    client.close()