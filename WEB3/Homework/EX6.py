from EX1 import db

# 1. Select collection:
river_collection = db["river"]

# 2. Add a list all river in "Africa" continent:
america_river = []

if __name__ == "__main__":
    river_list = river_collection.find(
        {
            "length": { "$gt":1000 },
        }
    )
    for river in river_list:
        if river["continent"] == "S. America":
            america_river.append(river)

print(america_river)