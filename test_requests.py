# -*- coding: utf-8 -*-
# script file for testing api

import requests
import json
import pandas as pd
from config import URL, API_KEY, PART


def get_info(part, headers):
    return requests.get(URL + part, headers=headers)


headers = {'api-key': API_KEY}


if __name__ == '__main__':
    # get response from api
    resp = get_info(PART, headers)
    # make json from responce text
    resp_dict = json.loads(resp.text)
    # get csv file from json
    df = pd.read_json(resp_dict)
    print(df.head())
