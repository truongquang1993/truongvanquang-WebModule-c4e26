from EX1 import db
import matplotlib.pyplot as plt

# 1. select collection
customers_collection = db["customers"]

# 2. add customer list for each ref:
ads_customers = []
events_customers = []
wom_customers = []

if __name__ == "__main__":    
    customers_list = customers_collection.find()

    for customer in customers_list:
        if customer["ref"] == "ads":
            ads_customers.append(customer)
        elif customer["ref"] == "events":
            events_customers.append(customer)
        else:
            wom_customers.append(customer)

# 3. Count and draw a pie chart:
slices = [len(ads_customers), len(events_customers), len(wom_customers)]
activities = ["Advertisement", "Events", "Word of mouth"]
colors = ["green", "blue", "red"]

plt.pie(
    slices,
    labels= activities,
    startangle= 90,
    autopct="%1.1f%%"
)
plt.show()

