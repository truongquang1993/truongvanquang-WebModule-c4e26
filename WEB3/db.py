from pymongo import MongoClient
uri = "mongodb+srv://admin:admin1@cluster0-f8q6q.mongodb.net/test?retryWrites=true"

#1. Connect
client = MongoClient(uri)
#2. Test Data base
db = client.test
# 3. Get collection
# def food_collection():

food_collection = db["food"]

# # 4. Create a new document
# new_food = {
#     "name": "Pho bo",
#     "price": 25000,
# }# document

# # 5. Insert new document into collection
# food_collection.insert_one(new_food)

# 6. Close connection
def close():
    client.close()
