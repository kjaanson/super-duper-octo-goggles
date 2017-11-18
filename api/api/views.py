
from api import app, log

from flask import jsonify

import os
import pickle

@app.route('/')
def index():
    log.info('index loaded')
    return 'Hello World!'



@app.route('/models', methods=['GET'])
def models():
    log.info('Available models:')

    models=[{
        'modelname':'model',
        'description':'Model docs/description',
    }]

    return jsonify(models)
