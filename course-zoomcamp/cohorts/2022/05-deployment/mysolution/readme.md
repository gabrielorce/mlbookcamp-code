
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