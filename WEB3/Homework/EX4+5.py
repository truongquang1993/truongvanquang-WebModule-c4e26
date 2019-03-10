from EX1 import db
# import pyexcel

# 1. Select collection:
river_collection = db["river"]

# 2. Add a list all river in "Africa" continent:
africa_river = []
if __name__ == "__main__":
    river_list = river_collection.find()
    for river in river_list:
        if river["continent"] == "Africa":
            africa_river.append(river)
            
print(africa_river)

# 3. Save as excell:
# pyexcel.save_as(records=africa_river, dest_file_name="Africa_river_list.xlsx")