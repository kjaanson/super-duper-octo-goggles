
from api import app, log

from flask import jsonify, request

import os
import pickle

import glob

import numpy as np
import pandas as pd

from .errors import abort

@app.route('/models', methods=['GET'])
def models():
    """Returns list of models that are served by the API."""
    log.info('Available models:')

    models = list()

    for modelpicklefile in glob.glob(os.path.join(app.config["MODELS_DIR"],"*.pickle")):
        basename = os.path.basename(modelpicklefile)
        modelname = os.path.splitext(basename)[0]

        model = pickle.load(open(modelpicklefile, "rb"))

        log.info(f'\nLoaded model {basename} \nModelname: {modelname}\nDesc: {model._desc_} \nInput features: {model._features_}')

        models.append({'modelname':modelname,
                       'description':model._desc_,
                       'input_features':model._features_})



    return jsonify(models)

@app.route('/models/<modelname>/predict', methods=['POST'])
def predict(modelname):
    """Makes prediction based on trained model. Takes JSON array of features as data.
    Order of features can be seen from the model._features_ instance variable.
    """

    avail_models = [os.path.splitext(os.path.basename(filename))[0]
                    for filename in glob.glob(os.path.join(app.config["MODELS_DIR"],"*.pickle"))]

    log.info(f"Available models: {avail_models}")

    if modelname not in avail_models:
        abort(404, f"Model '{modelname}' not found")

    model = pickle.load(open(os.path.join(app.config["MODELS_DIR"], f"{modelname}.pickle"), "rb"))

    post_data = request.get_json()

    if len(post_data)!=len(model._features_):
        abort(400, f"Number of presented features does not match the trained model.")

    predicted_class = model.predict(np.array([post_data])).tolist()

    return jsonify({'predicted_class':predicted_class})




