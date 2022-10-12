import pickle

model_file = "model1.bin"
dv_file="dv.bin"

with open(model_file, "rb") as f_in:
    model = pickle.load(f_in)

with open(dv_file, "rb") as f_in:
    dv = pickle.load(f_in)


client= {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

# turn this client into a feature matrix
X = dv.transform([client])

# probabilty that this culient gets a credit card
prediction=model.predict_proba(X)[0,1]

print (prediction)