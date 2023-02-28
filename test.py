import requests
import db as db

BASE = "http://localhost:5000/"

response = requests.get(BASE + "insert")
print(response.json())