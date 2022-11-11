Early Stage Diabetes risk Prediction Service  

---

The Early stage diabetes risk prediction dataset is available here:
[https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.)


The dataset contains the sign and symptom data of newly diabetic or would be diabetic patients.
We will use this dataset to train a model that will predict the probabilty of a person having diabetes.

The notebook uses the above link directly, but the same csv file is available in the data folder.




When we execute train.py, the model is created. The BentoML model tag is printed as an output. The prediction service can then utilize this model.

BentoML

To start the service, type:
```bash
bentoml serve predict.py:svc
```

But instead of using this locally, BentoML allows us to create a deployable, which is defined by the contents of the bentofile.yaml. To create this deployable, write:
```bash
bentoml build
```

If all went well, you should get a reply similar to this:
```bash
Successfully built Bento(tag="diabetes_risk_service:3xj4ktdbq6jrkaav").
```

You can now find the contents of this deployable in the bentoml directory. This directory includes a Dockerfile, requirements files, and the model itself.
To create the docker image, go to the directory which holds the dockerfile and write:
```bash
bentoml containerize diabetes_risk_service:3xj4ktdbq6jrkaav
```

The output of this execution also tells you how you can execute the container; which will be something like this:

```bash
docker run -it --rm -p 3000:3000 diabetes_risk_service:3xj4ktdbq6jrkaav serve --production
```


once the model is executed, you can access it via its URL:
http://localhost:3000/#/Service%20APIs/diabetes_risk_service__classify

A typical request would include this information in JSON format:

{
  "age": 0,
  "alopecia": "no",
  "delayed_healing": "yes",
  "gender": "no",
  "genital_thrush": "no",
  "irritability": "no",
  "itching": "no",
  "muscle_stiffness": "no",
  "obesity": "no",
  "partial_paresis": "no",
  "polyuria": "no",
  "polyphagia": "no",
  "polydipsia": "yes",
  "sudden_weight_loss": "yes",
  "visual_blurring": "no",
  "weakness": "yes"
}

And the output gives a probability that the person has diabetes.
