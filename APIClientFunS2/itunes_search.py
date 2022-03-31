import requests # a lib for HTTP requests
import json # a lib for parsing strings/JSON objects

url = "https://itunes.apple.com/search?"
# add our query terms
url += "term=thor&media=movie"

# make the GET request
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
response = requests.get(url)
# first check the status code
print("status code:", response.status_code)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status#successful_responses
if response.status_code == 200:
    # OK
    # parse the message body JSON
    json_obj = json.loads(response.text)
    print(type(json_obj))
    print(json_obj)
    # we want to the results list
    # then we will walk trhough each result object
    # and print out its name
    results_list = json_obj["results"]
    for result_obj in results_list:
        print(result_obj["trackName"])
        # task: print out the movie duration in hours

# task: create interview_predictor.py
# and parse the prediction from the URL given in 3.b.
# use the unseen instances from entropy lab task #2