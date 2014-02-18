#!/usr/bin/python
import requests
import json

path = ""

headers = {"Conent-Type": "text", "Authorization": "Client-ID 21073c5e8288f1d"}
urls = [
    "https://api.imgur.com/3/gallery/r/aww/top/day", "https://api.imgur.com/3/gallery/r/cats/top/day",
    "https://api.imgur.com/3/gallery/r/catgifs/top/day", "https://api.imgur.com/3/gallery/r/aww_gifs/top/day", 
    "https://api.imgur.com/3/gallery/r/animalgifs/top/day"]
links = []

for url in urls:
    r = requests.get(url, headers=headers, verify=False)
    data = json.loads(json.dumps(r.json()))

    for i in data['data']:
        links.append(i['link'])

# copy file to old list
try:
    with open(path + 'history.txt', 'a') as hist:
        with open(path + 'current.txt', 'r') as curr:
            for line in curr:
                hist.write(line)
except IOError as e:
    print("Error: file doesn't exist", e)

# download and write images
with open(path + 'current.txt', 'w') as curr:
    for url in links:
        curr.write(url + "\n")
