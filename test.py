import requests

response = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"data": [5.1, 3.5, 1.4, 0.2]}  # Change according to your model input
)
print(response.json())