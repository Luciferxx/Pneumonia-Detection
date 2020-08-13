import cv2
import numpy as np
import requests
import json
def pre_process(img):
    img=cv2.imread(img)
    resized = cv2.resize(img,(180,180))
    resized = np.array(resized,dtype=np.float32)
    resized= resized.reshape(-1,180,180,3)
    resized=resized/255
    return resized
def predict(img):
    img=pre_process(img)
    MODEL_URL = "https://saved-model1.herokuapp.com/v1/models/saved_model1:predict"
    data = json.dumps({
    "signature_name": "serving_default",
    "instances": img.tolist()
    })
    headers = {"content-type": "application/json"}
    response = requests.post(url=MODEL_URL, data=data, headers=headers)
    response.raise_for_status()
    response = response.json()
    prediction = np.squeeze(response['predictions'][0])
    if prediction >= 0.5:
        result=1
    else:
        result=0
    return result

    
    
