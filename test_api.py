import requests

res = requests.post(
    "http://127.0.0.1:8000/predict",
    json={"size": 85.0, "rooms": 3, "garden": 1}
)
print(res.json())