Introduction
============

Data transformation, model training and deployment task for Mindtitans.
I have used pandas and sklearn for initial data transformation and model training. Trained models are pickeled and
 stored in `.\models` directory where they are read by API. Snakemake pipeline is used for running model retraining etc.
 Flask API is minimal and only gives the predicted classification (rating).

Setup
=====

```
pip install -e requirements.txt
```

Pipeline
============

Data wrangling, model training and deployment pipeline is done using `pandas`, `sklearn` and `snakemake`. To
build model pickles for API run:
```
snakemake api/model_pickles/logregression.pickle
```

Deploying API
=============
After model(s) have been trained by pipeline run API:
```
python api/main.py
```

API uses models from `api/model_pickles` directory for predictions on data. Each should be pickled instance with the
 following:
  * `predict` method that takes in array of features to perform prediction on. This must be 2D array with size `(n_samples, n_features)`
  * `_desc_` human readable string for the model description
  * `_features_` list of feature names and their order that should be passed on to `predict` method for each sample

### API endpoints

  * `GET models/` - displays list of models, descriptions and their input feature orders

#### Sample API call
```
curl -X GET http://localhost:5000/models
```

  * `POST models/<modelname>/predict` - performs prediction on model using posted array of features

#### Sample API call
```
curl -X POST \
  http://localhost:5000/models/logreg/predict \
  -H 'content-type: application/json' \
  -d '[0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]'
```
