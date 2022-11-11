import numpy as np
import bentoml
from bentoml.io import NumpyNdarray
from pydantic import BaseModel
from bentoml.io import JSON


# Setting up data validation class
class DiabetesParameters(BaseModel):
    age: float
    alopecia: str
    delayed_healing: str
    gender: str
    genital_thrush: str
    irritability: str
    itching: str
    muscle_stiffness: str
    obesity: str
    partial_paresis: str
    polyuria: str
    polyphagia: str
    polydipsia: str
    sudden_weight_loss: str
    visual_blurring: str
    weakness: str

coolmodel_ref = bentoml.xgboost.get("diabetes_risk_model:latest")
dv = coolmodel_ref.custom_objects['dictVectorizer']

coolmodel_runner = coolmodel_ref.to_runner()

svc = bentoml.Service("diabetes_risk_service", runners=[coolmodel_runner])

@svc.api(input=JSON(pydantic_model=DiabetesParameters), output=JSON())
def classify(diabetes_risk_prediction):
    pred_dict = dv.transform(diabetes_risk_prediction.dict())
    result = coolmodel_runner.predict.run(pred_dict)
    return result [0]