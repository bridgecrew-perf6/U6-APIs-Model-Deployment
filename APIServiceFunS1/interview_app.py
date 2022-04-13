# we are going to use the flask micro web framework
# for our web app (run an API service with /predict
# endpoint)
import os
import pickle
from flask import Flask, jsonify, request

# now we create a flask app
# by default flask run on port 5000
app = Flask(__name__)

# now we need to define "routes"
# a route is a function that handles a request
# lets have a route for the root index page
@app.route("/", methods=["GET"])
def index():
    # we can return content and status code
    return "<h1>Welcome to my app!!</h1>", 200

# now the /predict route
@app.route("/predict", methods=["GET"])
def predict():
    # we need to parse the unseen instance's
    # attribute values from the request
    level = request.args.get("level", "") # "" default value
    lang = request.args.get("lang", "")
    tweets = request.args.get("tweets", "")
    phd = request.args.get("phd", "")
    print("level:", level, lang, tweets, phd)

    # TODO: fix the hardcoding
    prediction = predict_interviewed_well([level,
        lang, tweets, phd])
    # if anything goes wrong, predict_interviewed_well()
    # is going to return None
    if prediction is not None:
        result = {"prediction": prediction}
        return jsonify(result), 200
    return "Error making prediction", 400

def predict_interviewed_well(instance):
    # we need to traverse the interview tree
    # and make a prediction for instan
    # how do we get the tree here?
    # generally, we need to save a trained
    # ML mode from another process for use later
    # (in this process)
    # enter pickling
    # unpickle tree.p
    infile = open("tree.p", "rb")
    header, tree = pickle.load(infile)
    infile.close()

    print("header:", header)
    print("tree:", tree)
    # prediction time!!
    try:
        prediction = tdidt_predict(header, tree, instance)
        return prediction
    except:
        print("error")
        return None

def tdidt_predict(header, tree, instance):
    # recursively traverse tree to make a prediction
    # are we at a leaf node (base case) or attribute node?
    info_type = tree[0]
    if info_type == "Leaf":
        return tree[1] # label
    # we are at an attribute
    # find attribute value match for instance
    # for loop
    att_index = header.index(tree[1])
    for i in range(2, len(tree)):
        value_list = tree[i]
        if value_list[1] == instance[att_index]:
            # we have a match, recurse
            return tdidt_predict(header, value_list[2], instance)


if __name__ == "__main__":
    # deployment notes
    # we need to get our web app on the web
    # we can setup/maintain our own server OR
    # we can use a cloud provider
    # lots of cloud providers: AWS, GCP, Azure, DigitalOcean, 
    # Heroku, ...
    # we are going to use Heroku (PaaS platform as a service)
    # lots of ways to deploy a Flask app to Heroku
    # see my youtubes videos for 4 different ways
    # we will do what I call 2.B.
    # deploying a docker container using heroku.yml and git
    # first, we need to change some app settings
    # heroku is going to set the port for our app
    # to use via an enviroonment variable
    port = os.environ.get("PORT", 5000)
    app.run(debug=False, port=port, host="0.0.0.0") # TODO: turn off debug
    # when you deploy to production