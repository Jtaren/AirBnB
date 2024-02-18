#!/usr/bin/python3

import json

data = {
    "name" : "John",
    "age" : 21,
    "course" : ["Maths", "History", "Computer Science"]
}

# Convert to json formatted string
json_string = json.dumps(data)
# print(json_string)

# Save to a file
with open("data.json", "w") as json_file:
    json_file.write(json_string)