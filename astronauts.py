import requests 
import json 

f = r"http://api.open-notify.org/astros.json"
data = requests.get(f)
tt = json.loads(data.text)    

print("There are " + str(tt["number"]) + " astronauts in space right now.\n")

print("Their names are:\n----------------\n")
for i in range(tt["number"]):
	print(tt["people"][i]["name"])
