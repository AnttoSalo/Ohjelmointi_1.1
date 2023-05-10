import urllib.request
import json

url = "https://api.chucknorris.io/jokes/random"
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

print(data["value"])

# Antaa 403, en ymmärrä miksi
