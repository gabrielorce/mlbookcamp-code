import pickle
from flask import Flask, request, jsonify

# local solution works with local model1.bin, but instructor's docker image works with model2.bin included in image
model_file = "model2.bin"
dv_file="dv.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)

app = Flask('score')

# client= {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}


@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    # turn this client into a feature matrix
    X = dv.transform([client])

    # probabilty that this culient gets a credit card
    prediction=model.predict_proba(X)[0,1]
    
    result = {
        'credit_card_probability': float(prediction),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)
