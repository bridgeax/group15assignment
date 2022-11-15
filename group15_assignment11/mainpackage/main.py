# main.py
import json # Built in, no pip required
import requests

response = requests.get('https://api.epa.gov/FACT/1.0/facilities?api_key=ZeUwluaLFDBtlpaqJzwm7bR9D4YLUx8G1kFBklkl')
json_string = response.content

parsed_json = json.loads(json_string) # Now we have a python dictionary

#print(parsed_json)
#print(parsed_json['data'][0]['orisCode'])
#print(parsed_json['data'][0]['name'])

for facilities in parsed_json['data']:
    print("Oris Code :", facilities["orisCode"])
    print("Geographic Location :", facilities["geographicLocation"])
    print("Name :", facilities["name"])