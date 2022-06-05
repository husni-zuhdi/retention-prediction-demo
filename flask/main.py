import os
import json
import pickle
import numpy as np
from crypt import methods
from dotenv import load_dotenv
from flask import Flask, request
from tensorflow.python.keras.models import model_from_json

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/predict", methods = ["POST"])
def predict():
    data = request.get_json()
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
    elif data["department"] == "product_mng":
        data["department_product_mng"] = 1
    elif data["department"] == "marketing":
        data["department_marketing"] = 1
    del data["department"]

    if data["salary_level"] == "low":
         data["salary_level_low"] = 1
    elif data["salary_level"] == "medium":
        data["salary_level_medium"] = 1
    elif data["salary_level"] == "high":
        data["salary_level_high"] = 1
    del data["salary_level"]

    print(data["id"])

    # loading model
    model = model_from_json(open(os.environ.get("MODEL_LAYER")).read())
    model.load_weights(os.environ.get("MODEL_WEIGHTS"))

    # dont forget to compile your model
    model.compile(loss='binary_crossentropy', optimizer='adam')

    # and load standard_scaler
    with open(os.environ.get("STANDARD_SCALER"), 'rb') as handler:
        sc = pickle.load(handler)

    # model_pred = model.predict(sc.transform(np.array([data])))
    model_pred = {"hello": data}
    
    return model_pred


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))