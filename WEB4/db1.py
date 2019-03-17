from pymongo import MongoClient
uri = "mongodb+srv://admin:admin1@cluster0-f8q6q.mongodb.net/test?retryWrites=true"

#1. Connect
client = MongoClient(uri)
#2. Test Data base
db1 = client.test
# 3. Get collection

user_collection = db1["user"]

# 6. Close connection
def close():
    client.close()
