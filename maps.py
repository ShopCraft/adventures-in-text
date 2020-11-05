'''
Map Game Data. Descriptions of the locations in the game world (metro stations).
'''
import requests, json

metroapi="https://api.metro.net/agencies/lametro-rail/"
trains="/agencies/lametro-rail/"

print(metroapi)

response = requests.get(metroapi)
json_response = response.json()

print(response)
print(json_response)

print(json.dumps(json_response, indent=1))