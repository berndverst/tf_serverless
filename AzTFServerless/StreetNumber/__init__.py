import json
import os
import sys

import azure.functions as func
from requests_toolbelt import MultipartDecoder

from . import gan_model


'''
Declare global objects living across requests (TODO: investigate this)
'''

current_location = os.path.dirname(os.path.realpath(__file__))
model_dir = os.path.dirname(os.path.realpath(__file__)) + '/model'
model = gan_model.GANModel(model_dir)


def main(req: func.HttpRequest) -> func.HttpResponse:
    '''
    HTTP request handler for our Tensorflow prediction API.

    Assumes a jpg or gif image is uploaded in a POST request body as multipart/form-data.
    '''
    try:
        image_bytes = req.get_body()

        content_type = req.headers.get("Content-Type")
        formdatadecoder = MultipartDecoder(image_bytes, content_type)

        # assumes there is only one part (our single image file) being uploaded
        for part in formdatadecoder.parts:
            resp_body = predict(part.content)
            break
 
        return func.HttpResponse(
            status_code=200,
            headers={"Content-Type": "application/json"},
            body=json.dumps(resp_body)
        )

    except Exception as e:
        raise e
        return func.HttpResponse(
             "Either you did not post a compatible image or an unknown error occurred.",
             status_code=500
        )

    return func.HttpResponse()
       

def predict(image_bytes):
    '''
    Inferencing method to retrieve prediction result from model.
    '''

    results = model.predict(image_bytes)
    results_json = [{'digit': str(res[0]),
                     'probability': str(res[1])} for res in results]
    print('Results retrieved: {}'.format(results_json))
     
    return {'prediction_result': results_json}
