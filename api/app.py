from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("../model/model.pkl")

@app.route('/detect', methods=['POST'])
def detect():
   data = request.json['features']
   prediction = model.predict([data])

   return jsonify({
       "prediction": int(prediction[0])
   })

if __name__ == "__main__":
   app.run(debug=True)