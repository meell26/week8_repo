from flask import Flask, request, jsonify
import joblib
import pandas as pd

from agents.agents import detector, analyzer, reporter

app = Flask(__name__)

model = joblib.load("model/model.pkl")

@app.route('/')
def home():
   return "Threat Intelligence API is running "

@app.route('/detect', methods=['POST'])
def detect():
   try:
       data = request.json

       features = pd.DataFrame([{
           "failed_logins": data["failed_logins"],
           "request_count": data["request_count"]
       }])

       prediction = model.predict(features)[0]

       # agents
       d = detector(prediction)
       a = analyzer(prediction)
       r = reporter(a)

       return jsonify({
           "prediction": int(prediction),
           "detection": d,
           "analysis": a,
           "alert": r
       })

   except Exception as e:
       return jsonify({"error": str(e)})

if __name__ == "__main__":
   app.run(debug=True)