# Copyright 2019 IBM Corporation 
# 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
# 
#     http://www.apache.org/licenses/LICENSE-2.0 
# 
# Unless required by applicable law or agreed to in writing, software 
# distributed under the License is distributed on an "AS IS" BASIS, 
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. 
# See the License for the specific language governing permissions and 
# limitations under the License. 
import os
import json

from flask import Flask, request, abort
from flask_cors import CORS

import torch
import numpy as np
from torch.autograd import Variable
from minio import Minio

import zipfile
import importlib
import re


""" Model prediction """
class Model():
    def __init__(self):
        training_id = os.environ.get("TRAINING_ID")
        endpoint_url = os.environ.get("BUCKET_ENDPOINT_URL")
        bucket_name = os.environ.get("BUCKET_NAME")
        bucket_key = os.environ.get("BUCKET_KEY")
        bucket_secret = os.environ.get("BUCKET_SECRET")
        model_file_name = os.environ.get("MODEL_FILE_NAME")
        model_class_name = os.environ.get("MODEL_CLASS_NAME")
        model_class_file = os.environ.get("MODEL_CLASS_FILE")

        # Define Object Storage resource and download the model file

        url = re.compile(r"https?://")
        cos = Minio(url.sub('', endpoint_url),
                    access_key=bucket_key,
                    secret_key=bucket_secret)

        KEY = training_id + '/' + model_file_name

        model_files = training_id + '/_submitted_code/model.zip'
        cos.fget_object(bucket_name, KEY, 'model.pt')
        cos.fget_object(bucket_name, model_files, 'model.zip')

        # Load PyTorch model definition from the source code.
        zip_ref = zipfile.ZipFile('model.zip', 'r')
        zip_ref.extractall('model_files')
        zip_ref.close()

        modulename = 'model_files.' + model_class_file.split('.')[0].replace('-', '_')

        '''
        We required users to define where the model class is located or follow
        some naming convention we have provided.
        '''
        model_class = getattr(importlib.import_module(modulename), model_class_name)

        device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        self.model = model_class().to(device)
        self.model.load_state_dict(torch.load('model.pt', map_location=device))
        self.model.eval()

    def predict(self, X):
        return self.model(torch.FloatTensor(X)).tolist()


app = Flask(__name__)
CORS(app)
model = Model()


""" API methods. """
@app.route('/predict', methods=['POST'])
def serving_api():
    try:
        inputs = request.json['inputs']
        global model
    except:
        abort(400)
    return json.dumps({"predictions": model.predict(inputs)})


@app.route('/predict', methods=['OPTIONS'])
def serving_api_options():
    return "200"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
