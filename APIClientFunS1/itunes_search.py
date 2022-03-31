import requests # a lib for making HTTP requests
import json # a lib for parsing strings/JSON objects

url = "https://itunes.apple.com/search?"
# add query terms
url += "term=thor&media=movie"

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
    # we want the results list so we can iterate through
    # each result JSON object
    # and grab the result's trackName (movie name)
    results_list = json_obj["results"]
    for result_obj in results_list:
        print(result_obj["trackName"])
        # task: print out the movie duration in hours
# task: in interview_predictor.py make a request for the interview_well
# class label for our unseen instance(s) on Entropy lab task #2


