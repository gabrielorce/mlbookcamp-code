## pipenv

First install pipenv, if not already instlled:
```bash
pip install pipenv
```


Go to the directory of interest and install the virtual environment:
```bash
pipenv install
```

Now activate the environment you just created:
```bash
pipenv shell
```

Now you can install a requirement:
```bash
pipenv install requests
```

to get the locaition of the virtual environment:
```bash
pipenv --venv
```

## THIS SOLUTION:
```bash
pipenv install bentoml
```

version:
```bash
bentoml -version
```

get model list (including model size):
```bash
bentoml models list
```

get model information, including things such as framework versions:
```bash
bentoml models get credit_risk_model:whht3gkvr6c6n3fr
```

build a model when you have the yaml descriptor on the same dir
```bash
bentoml build
```

containerize the build (this creates a docker image)
```bash
bentoml containerize credit_risk_model:whht3gkvr6c6n3fr
```


Install Pydantic
```bash
pip install pydantic
```

Question 4: Use this
```bash
curl -O https://s3.us-west-2.amazonaws.com/bentoml.com/mlzoomcamp/coolmodel.bentomodel
bentoml models import coolmodel.bentomodel
```
NOTE: This imported the model as "mlzoomcamp_homework:qtzdz3slg6mwwdu5"



Question 5:  Need sklearn
```bash
pip install sklearn
```

create service.py. When done execute this to start the model as a service:
```bash
bentoml serve service:svc --reload
```

Question 6:  Need locust
```bash
pip install locust
```

copy locust.py file and execute test. Then dowload 2nd model and import it:
```bash
curl -O https://s3.us-west-2.amazonaws.com/bentoml.com/mlzoomcamp/coolmodel2.bentomodel
bentoml models import coolmodel2.bentomodel
```

