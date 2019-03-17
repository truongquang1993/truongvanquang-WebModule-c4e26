from db import food_collection
from bson import ObjectId

def add_new_food(name, price):
    new_food = {
        "name": name,
        "price": price,
    }
    food_collection.insert_one(new_food)

def get(query): #filter, limit, skip
    food_list = food_collection.find(query)
    return food_list 

def get_by_id(id):
    f = food_collection.find_one({ "_id": ObjectId(id) })
    return f

def del_by_id(id):
    food_collection.delete_one({ "_id": ObjectId(id) })

def update_by_id(id, name, price):
    query = { "_id": ObjectId(id) }
    updater = {
        "$set": { "price": price },
        "$set": { "name": name },
    } # $inc, $dec, $set, $unset
    food_collection.find_one_and_update(query, updater)

# def find_by_username(username):

if __name__ == "__main__":
    # print(*get({}))
    f = get_by_id("5c8a5a931c9d440000d9ba28")
    if f != None:
        print(f)
    else:
        print("Not found")
    # for food in get({ "_id": ObjectId('5c8124e84fba13219419beee') }):
    #     print(food)
