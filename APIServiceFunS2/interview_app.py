# we are going to use the flask micro web framework
# for our web app (running our API service)
import pickle
from flask import Flask, jsonify, request

# create our web app
# flask runs by default on port 5000
app = Flask(__name__)

# we are now ready to setup our first "route"
# route is a function that handles a request
@app.route("/", methods=["GET"])
def index():
    # we can return content and status code
    return "<h1>Welcome to my app!!</h1>", 200

# now for the /predict endpoint
@app.route("/predict", methods=["GET"])
def predict():
    # parse the query string to get our
    # instance attribute values from the client
    level = request.args.get("level", "") # "" is default value
    lang = request.args.get("lang", "")
    tweets = request.args.get("tweets", "")
    phd = request.args.get("phd", "")
    print("level:", level, lang, tweets, phd)

    # TODO: fix the hardcoding
    prediction = predict_interviewed_well([level,
        lang, tweets, phd])
    # if anything goes wrong in predict_interviewed_well,
    # it will return None
    if prediction is not None:
        result = {"prediction": prediction}
        return jsonify(result), 200
    return "Error making prediction", 400

def predict_interviewed_well(instance):
    # we need a ML model to make a prediction for 
    # instance 
    # typically the model is trained "offline" 
    # and used later "online" (e.g. via this web app)
    # enter pickling
    # unpickle tree.p into header and tree
    infile = open("tree.p", "rb")
    header, tree = pickle.load(infile)
    infile.close()

    print("header:", header)
    print("tree:", tree)

    try:
        prediction = tdidt_predict(header, tree, instance)
        return prediction
    except:
        print("error")
        return None

def tdidt_predict(header, tree, instance):
    # recursively traverse the tree
    # we need to know where we are in the tree...
    # are we at a leaf node (base case) or
    # attribute node
    info_type = tree[0]
    if info_type == "Leaf":
        return tree[1]
    # we need to match the attribute's value in the
    # instance with the appropriate value list
    # in the tree
    # a for loop that traverses through
    # each value list
    # recurse on match with instance's value
    # TODO: finish this

if __name__ == "__main__":
    app.run(debug=True, port=5001) # TODO: turn debug off
    # when deploy to "production"