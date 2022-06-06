# Retention Prediction for CC-25
> 🇮🇩 Part of Bangkit 2022

> 🛑 Please use it wisely! Remeber Bangkit 2022 Code of Conduct!
**Use it as reference only!**

## Stack used
1. 🤖 Tensorflow 2.8
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
### ⚡️ Deploy MySQL Database in Compute Engine
2. Run `export PROJECT_ID=$(gcloud config get-value project)`
3. Run `docker build -t gcr.io/$PROJECT_ID/retention-pred:v1.0 .`
4. Run `gcloud auth configure-docker` and press `Y`
5. Run `docker push gcr.io/$PROJECT_ID/retention-pred:v1.0`
6. Run `gcloud run deploy --image gcr.io/$PROJECT_ID/retention-pred:v1.0 --platform managed`
7. Check your GCP Console > Cloud Run

## References : 

[1] https://www.digitalocean.com/community/tutorials/how-to-build-a-deep-learning-model-to-predict-employee-retention-using-keras-and-tensorflow

[2] https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service