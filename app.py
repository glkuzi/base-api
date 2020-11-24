# -*- coding: utf-8 -*-

from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
import os
import json
import pandas as pd
from config import PREDICTIONS_PATH, API_KEY

app = Flask(__name__)
api = Api(app)

todos = {}

parser = reqparse.RequestParser()
parser.add_argument('api-key', location='headers')


class BasePredictions(Resource):
    @api.representation('application/json')
    def get(self, day):
        # check api key
        args = parser.parse_args()
        if args['api-key'] != API_KEY:
            code = 404
            resp = make_response('Auth error - check api key', code)
            return resp
        # for now, day could be 'today' or 'tomorrow'
        if day == 'today':
            fname = os.path.join(PREDICTIONS_PATH,
                                 'today' + '.csv')
            df = pd.read_csv(fname)
            data = df.to_json()
            resp = make_response(json.dumps(data), 200)
        elif day == 'tomorrow':
            fname = os.path.join(PREDICTIONS_PATH,
                                 'tomorrow' + '.csv')
            df = pd.read_csv(fname)
            data = df.to_json()
            resp = make_response(json.dumps(data), 200)
        else:
            code = 404
            resp = make_response('File not found', code)
        return resp


api.add_resource(BasePredictions, '/<string:day>')

if __name__ == '__main__':
    app.run(debug=False)
