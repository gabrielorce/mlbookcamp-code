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

to get the locaiton of the virtual environment:
```bash
pipenv --venv
```


## This solution
In this directory we have:
predict-score-selcontained.py: model and query in same file. No web service.

predict-score-web.py: model and web server contained here. Called by "test-request"
the latter can be called by this command:


```bash
pipenv run gunicorn --bind 0.0.0.0:9696 predict-score-web:app
```

but ultimately this all goes into the dockerfile.

The docker image was built with:
```bash
docker build -t zoomcamp-hw5 .
```

The docker image can be run with:
```bash
docker run -it --rm -p 9696:9696 zoomcamp-hw5
```