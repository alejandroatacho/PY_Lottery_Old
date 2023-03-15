import time

community_building_appartements_low = {
    "name": "Community Building Appartements Low",
    "type": "building",
    "price": 125000,
    "rent": 700,

}

community_building_appartement_medium = {
    "name": "Community Building Appartements",
    "description": "Medium sized appartements for the community",
    "price": 200000,
    "rent": 1000}

community_building_appartements_high = {
    "name": "Community Building Appartements High",
    "description": "High end appartements for the community",
    "price": 400000,
    "rent": 2000}

holder = "\nAlejandro Atacho\n┊┊┊┊╭━━╮╭━━╮┊╭━┓\n┈╭━━┫▔╲┣╯━━┻╮┃╭┛♫\n╭┫┈┈┃┈┈▏┊▋┊▋┃┃┃\n┃┃┈┈┃┈╱╭╰╯╰╯╰┫┣━╮\n╯┃┈┈╰━━╯╰━━━┳┫┣╮┃\n┈┃╭┳╭━┫╭┳╭━━╯┃┃┃┃\n┈┃┃┃┃┈┃┃┃┃┈╭╮┃╰╯┃\n┈┗┛┗┛┈┗┛┗┛╭╮┈╰━━╯"
print(".")
time.sleep(1)
print("...")
time.sleep(1)
print("......")
print (holder)
time.sleep(1)
print("Community Building Appartements Rental Service Is Initiated")

print("The current prices are consider in the following way from low, medium, high: \n",community_building_appartements_low["price"], community_building_appartement_medium["price"], community_building_appartements_high["price"])

while 1 == True:
    print("Pick a community building: ", community_building_appartements_low["name"], community_building_appartement_medium["name"], community_building_appartements_high["name"])
    print("What type of community building do you want to rent?: Low, Medium, High")
    print("Type Below: Low or Medium and High")
    user_input = input()
    if user_input == "low" or user_input == "Low":
        print("This is the current prices for the low community appartments", (community_building_appartements_low))
        print("This appartment monthly rent is: ", (community_building_appartements_low["rent"]))
        break
    elif user_input == "medium" or user_input == "Medium":
        print("This is the current prices for the medium community appartments", community_building_appartement_medium)
        print("This appartment monthly rent is: ", (community_building_appartement_medium["rent"]))

        break
    elif user_input == "high" or user_input == "High":
        print("You have rented the high community appartments", (community_building_appartements_high))
        print("This appartment monthly rent is: ", (community_building_appartements_high["rent"]))

        break
    else:
        print("Please enter a valid input")
        continue

# community building
# {   
#     many different price ranges (for customer classes)
#     in order to pay the prices of the provided stores/media/entertaintment buildings.    
# }


# while community_building {
    
# }
# parking space


