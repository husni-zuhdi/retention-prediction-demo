# Retention Prediction for CC-25
> 🇮🇩 Part of Bangkit 2022

> 🛑 Please use it wisely! Remeber Bangkit 2022 Code of Conduct!
**Use it as reference only!**

## Stack used
1. 🤖 Tensorflow 2.9
2. 🍾 Flask 2.10

## Google Cloud Service used
1. ⚡️ Cloud Run

## Local requirements
1. 🐍 Python 3
2. 🐳 Docker
3. 🚦 Any IDE you like

## 👨🏽‍💻 How to use in local
### 📒 Notebook
1. Clone this repositroy
2. Run `python install -r requirements.txt`
3. Open the `retention-prediction.ipynb`

### 🔥 API (Flask)
> Please ignore the `expressjs` folder. It's my failure 🥲
1. Clone this repositroy
2. Open flask folder
3. Run `python install -r requirements.txt`
4. Create `.env` file in root folder with this specifications

| Variables             | Function                          | Example       |
| --------------------- |:--------------------------------: | -------------:|
| PORT                  | your_API_port                     | 8081          |
| MODEL_LAYER           | your_model_layer_path             | model.json    |
| MODEL_WEIGHTS         | your_model_weights_path           | weights.h5    |
| STANDARD_SCALER       | your_standard_scaler_path (opt)   | sc.pkl        |

5. Run `docker build -t retention-pred:v1.0 .`
4. Run `export PORT=your_API_port` change to match API port
4. Run `docker run --name retention-prediction -p 0.0.0.0:$PORT:$PORT -d retention-pred:v1.0`
5. Test with Postman or CLI

## ☁️ How to use in Cloud
### ⚡️ Deploy ML API with Cloud Run

#### ✅ First, let's create our Service account
> 🚨 This still in development. Please jump to the second step

1. Run `export PROJECT_ID=$(gcloud config get-value project)`
2. Run `export SA=retention-prediction`
2. Run this to create `retention-prediction` service account
```
gcloud iam service-accounts create $SA \
    --description="retention-prediction SA" \
    --display-name="retention-prediction"
```
3. Run this to bind service account with `Storage Admin` role
```
gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member="serviceAccount:$SA@$PROJECT_ID.iam.gserviceaccount.com" \
    --role="roles/storage.admin"
```
4. Run this to get service account key as `key.json`
```
gcloud iam service-accounts keys create key.json \
    --iam-account=$SA@$PROJECT_ID.iam.gserviceaccount.com
```
5. Add `s` into the `.env` file

| Variables                      | Function                  | Example       |
| ------------------------------ |:------------------------: | -------------:|
| GOOGLE_APPLICATION_CREDENTIALS | your_service_account_path | ./key.json    |

6. 🚨 Keep it secret okay. Don't push your service account key into the github!


#### ✅ Then we're ready to deploy our Cloud Run

1. Run `docker build -t gcr.io/$PROJECT_ID/retention-pred:v1.0 .`
2. Run `gcloud auth configure-docker` and press `Y`
3. Run `docker push gcr.io/$PROJECT_ID/retention-pred:v1.0`
4. Run `gcloud run deploy --image gcr.io/$PROJECT_ID/retention-pred:v1.0 --platform managed`
5. Check your GCP Console > Cloud Run

## Misc

* If you encounter error below, run `sudo apt install python3-tk`
```
ModuleNotFoundError: No module named 'tkinter'
```

## References : 

[1] https://www.digitalocean.com/community/tutorials/how-to-build-a-deep-learning-model-to-predict-employee-retention-using-keras-and-tensorflow

[2] https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service