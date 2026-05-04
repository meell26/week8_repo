import requests

url = "http://127.0.0.1:5000/detect"

data = {
   "failed_logins": 5,
   "request_count": 20
}

response = requests.post(url, json=data)

print("Response from API:")
print(response.json())