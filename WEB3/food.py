from db import food_collection

def add_food(name, price):
    new_food = {
        "name": name,
        "price": price,
    }
    food_collection.insert_one(new_food)

def get():
    food_list = food_collection.find()
    return food_list

if __name__ == "__main__":    
    # start = "yes"
    # while start == "yes":
    #     new_name = input("New name of data:")
    #     price_of_new_name = int(input("Price of new name:"))
    #     add_food(new_name, price_of_new_name)
    #     start = input("Do you want insert new data? (yes/no)")
    
    food_list = food_collection.find(
        {
            "price": { "$gt":25000 },
        }
    )
    # print(food_list[1]["name"])
    # print(food_list[1]["price"])

    for food in food_list:
        print(food["name"])
        print(food["price"])