from pymongo import MongoClient
import json # to read json files easier
import os # to make sure that the inputted json file exits

# ask for json filename
while True:
    json_name = input("Enter json file name with the .json extension: ")
    # verify that json file exists
    if os.path.exists(f"./{json_name}") == True:
        break
    else:
        print("file not found\n")

# convert json file into list
file = open(json_name, "r")
data = []
for line in file:
    data.append(json.loads(line))

# this part just prints to see if i did this right (i think i did????)
for i in data:
    print(i)
    print()



# ask for port number
while True:
    port_num = input("Enter a 5 digit port number: ")
    
    # verify the port number is valid
    if (port_num.isdigit() == False) or (len(str(port_num)) != 5 ):
        print("invalid entry\n")
    else:
        break

# create mongo server with user given port number
# have not checked what to do with the mongoclient yet will work on it later
client = MongoClient('localhost', int(port_num))
