'''
Created on Oct 24, 2022
Name: Alex Bridge, Matthew Lamb
email: bridgeax@mail.uc.edu, Lambmj@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can use an API key and parse a dictionary.
Citations: N/A
Anything else that's relevant:
'''
# main.py
import json # Built in, no pip required
import requests


response = requests.get('https://api.epa.gov/FACT/1.0/facilities?api_key=ZeUwluaLFDBtlpaqJzwm7bR9D4YLUx8G1kFBklkl')
json_string = response.content

parsed_json = json.loads(json_string) # Now we have a python dictionary

#print(parsed_json)
#print(parsed_json['data'][0]['orisCode'])
#print(parsed_json['data'][0]['name'])

# parsing 
for facilities in parsed_json['data']:
    print("Oris Code :", facilities["orisCode"])
    print("Geographic Location :", facilities["geographicLocation"])
    print("Name :", facilities["name"])
    print("County :", facilities["county"])

    
  
# Extract data from a dictionary and print to console
# Let's find out the code for Auglaize County

thisdict =    {
  "County": "Auglaize County",
  "Code": "OH011",
}
for x in thisdict.values():
  print(x)
