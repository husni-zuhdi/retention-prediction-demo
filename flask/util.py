import os
import json
import pickle
# from pyexpat import model
# import gcsfs
import numpy as np
from turtle import update
from tensorflow.python.keras.models import model_from_json

def transform(request_json):
    # load the json request data
    data = dict(request_json)

    # insert additional data
    adds_data = {
        "department_sales": 0,
        "department_accounting": 0,
        "department_hr": 0,
        "department_technical": 0,
        "department_support": 0,
        "department_management": 0,
        "department_IT": 0,
        "department_RandD": 0,
        "department_product_mng": 0,
        "department_marketing": 0,
        "salary_level_low": 0,
        "salary_level_medium": 0,
        "salary_level_high": 0
    }
    # and update with new additional data
    data.update(adds_data)

    # hell of if else to match with model input layer spec
    if data["department"] == "sales":
         data["department_sales"] = 1
    elif data["department"] == "accounting":
        data["department_accounting"] = 1
    elif data["department"] == "hr":
        data["department_hr"] = 1
    elif data["department"] == "technical":
        data["department_technical"] = 1
    elif data["department"] == "support":
        data["department_support"] = 1
    elif data["department"] == "management":
        data["department_management"] = 1
    elif data["department"] == "IT":
        data["department_IT"] = 1
    elif data["department"] == "RandD":
        data["department_RandD"] = 1
    elif data["department"] == "product_mng":
        data["department_product_mng"] = 1
    elif data["department"] == "marketing":
        data["department_marketing"] = 1
    del data["department"]

    # i want to move to python3.10 right now. i want switch and case!!
    if data["salary_level"] == "low":
         data["salary_level_low"] = 1
    elif data["salary_level"] == "medium":
        data["salary_level_medium"] = 1
    elif data["salary_level"] == "high":
        data["salary_level_high"] = 1
    del data["salary_level"]

    # set np array wich compatible with model input layer
    predict_data = np.array([
        float(data["satisfaction_level"]),
        float(data["last_evaluation"]),
        float(data["number_project"]),
        float(data["average_montly_hours"]),
        float(data["time_spend_company"]),
        float(data["work_accident"]),
        float(data["promotion_last_5years"]),
        float(data["department_IT"]),
        float(data["department_RandD"]),
        float(data["department_accounting"]),
        float(data["department_hr"]),
        float(data["department_management"]),
        float(data["department_marketing"]),
        float(data["department_product_mng"]),
        float(data["department_sales"]),
        float(data["department_support"]),
        float(data["department_technical"]),
        float(data["salary_level_high"]),
        float(data["salary_level_low"]),
        float(data["salary_level_medium"])
    ])
    return predict_data

def load_model():
    # loading model
    model = model_from_json(open(os.environ.get("MODEL_LAYER")).read())
    model.load_weights(os.environ.get("MODEL_WEIGHTS"))

    # dont forget to compile your model
    model.compile(loss='binary_crossentropy', optimizer='adam')

    # and load standard_scaler
    with open(os.environ.get("STANDARD_SCALER"), 'rb') as handler:
        sc = pickle.load(handler)

    ## experiment to use gcs
    ## still in development
    ## ====================
    # change your project name
    # PROJECT_NAME = 'browsing-project'
    # CREDS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    # MODEL_LAYER = os.environ.get("MODEL_LAYER")
    # MODEL_WEIGHTS = os.environ.get("MODEL_WEIGHTS")
    # STANDARD_SCALER = os.environ.get("STANDARD_SCALER")

    # FS = gcsfs.GCSFileSystem(project=PROJECT_NAME,
    #                         token=CREDS)

    # with FS.open(MODEL_LAYER, 'rb') as layer:
    #     new_model = model_from_json(layer.read())

    # with FS.open(MODEL_WEIGHTS, 'rb') as weights:
    #     new_model.load_weights(weights.read())
    #     new_model.compile(loss='binary_crossentropy', optimizer='adam')

    # with FS.open(STANDARD_SCALER, 'rb') as handler:
    #     sc = pickle.load(handler)
    
    return model, sc