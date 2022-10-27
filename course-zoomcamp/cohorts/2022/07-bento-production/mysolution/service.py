import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

coolmodel_runner = bentoml.sklearn.get("mlzoomcamp_homework:latest").to_runner()

svc = bentoml.Service("coolmodel_service", runners=[coolmodel_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result = coolmodel_runner.predict.run(input_series)
    return result