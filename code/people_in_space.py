import urllib.request
import json
import pprint

url = "http://api.open-notify.org/astros.json"

with urllib.request.urlopen(url) as response:
    response_text = response.read().decode("utf-8")
    # print(response_text)
    # print(type(response_text))
    data = json.loads(response_text)
    # print(data)
    # print(type(data))
    pprint.pprint(data)

# Can you print number of people in the space?


# Can you print all the names?
