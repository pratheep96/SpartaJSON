#JSON Javascript Object Notation
# Person = {
#     name: "John",
#     age: 25,
#     Speak: function(){
#         console.log(name)
#     }
# }

#Types of Data inside a JSON file
#JSON is a key value system or a large dictionary as we know it in Python
# "key" : "value"
# A string
# A number
# An object (JSON object)
# An array
# A boolean
# Null

# {
# "Trainer1" =  {
#         "name": "markson",
#         "age" : 25,
#         "job" : "mechanic",
#     },
# "Trainer2" = {
#        "name": "william",
#        "age" : 40,
#        "job" : "recruitment",
#     },
# }

import json
car_data = {"name": "tesla", "engine": "electric"}

# json.dumps() and json.dump()

car_data_json_string = json.dumps(car_data)
print(car_data_json_string)
print(car_data)

json_file = open("json_out_alternative.json", "w")

#This is an alternative to the statement above
with open("json_out_alternative.json", "w") as json_file2:
    json.dump(car_data, json_file)

with open('json_out.json') as open_json_file:
    electric_car = json.load(open_json_file)
    print(type(electric_car))
    print(electric_car['name'])
    print(electric_car['engine'])