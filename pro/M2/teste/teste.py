import json


f = open("json_HW.json",)
data = json.load(f)
for i in data["emp_details"]:
    print(i)