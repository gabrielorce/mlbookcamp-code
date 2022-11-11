# Early Stage Diabetes risk Prediction Service  


The Early stage diabetes risk prediction dataset is available here:
[https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.](https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+dataset.)


The dataset contains the sign and symptom data of newly diabetic or would be diabetic patients.
We will use this dataset to train a model that will predict the probabilty of a person having diabetes.

This project uses BentoML. BentoML allows you to create Machine Learning services that are ready to deploy and scale.

The notebook contains the analysis of the variables and the testing of the different potential models. It calls the dataset from the above link directly, but the same csv file is available in the data folder.

The file train.py creates the model that was found to be best for the job. Once it is executed, it prints out the BentoML model tag as part of its output. The prediction service can then utilize this model.

The predict.py file is the file that serves the model for consumption. When executed, it serves the model in a URL (if it is served locally, the URL is localhost:3000)

## BentoML

Once the model is created after executing the train.py file, we can use BentoML. 

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

```bash
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
```

And the output gives a probability that the person has diabetes.

---

## DEPLOYMENT TO AWS:

The steps to deploy to AWS are:
- Create an AWS account
- Download the AWS CLi tool, since you will need to use the command line
- Upload the docker image we created with BentoML. For this, go to the Elastic Container Registry section of AWS, create a new repository named "prediction-service", go into it and click on the "View Push commands" button on the top-right of the screen. This will explain the commands you hav to enter in your machine so you can push the image you built into this registry
- Once you have pushed the image, you can now use it. Go to AWS ECS (Elastic Container Service). Here you must first create a cluster ("prediction-service-cluster"). Once you have cretaed it, you must then go to "Task Definitions" to create a task (called "prediction-service-task"). Within this task you define a number of things, among them the container you will use.
- Once all these stes are complete, you can go back to your cluster, select the "Tasks" tab, and then clcik on the task name ("prediction-service-task") so you can see important information, including the URL through which the container is available.
- To access the server, place the URL and also the port number (<URL>:3000) on your web browser so you can interact with the prediction service.
  
  
I was able to complete the above steps; the container has been deployed to Amazon ECS, and the prediction service can be accessed at this URL: 
http://35.90.127.210:3000/
