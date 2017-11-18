from flask import Flask, jsonify, abort, make_response, request

from api import app

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error.description}), 404)

@app.errorhandler(401)
def custom401(error):
    return make_response(jsonify({'error': error.description}), 401)

@app.errorhandler(400)
def custom400(error):
    return make_response(jsonify({'error': error.description}), 400)
