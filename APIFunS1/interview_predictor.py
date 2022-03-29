import requests # a lib for making HTTP requests
import json # a lib for parsing strings/JSON objects

url = "https://interview-flask-app.herokuapp.com/predict?"
# add query terms
url += "level=Junior&lang=Java&tweets=yes&phd=yes"

# make the GET request
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
response = requests.get(url)
# first, check the status code
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses
print("status code:", response.status_code)

if response.status_code == 200:
    # then parse the message body (contains the JSON response)
    json_obj = json.loads(response.text)
    print(type(json_obj))
    print(json_obj)