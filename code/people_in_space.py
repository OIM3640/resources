import urllib.request
import json

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as f:
    response_text = f.read().decode('utf-8')
    j = json.loads(response_text)
    print(j)

# Can you print number of people in the space?


# Can you print all the names?
