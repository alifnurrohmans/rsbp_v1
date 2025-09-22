import requests
from requests.auth import HTTPBasicAuth
import json

# Konfig
URL = "https://5e0cad42.databases.neo4j.io/db/5e0cad42/query/v2"
USER = "5e0cad42"
PASSWORD = "v63KNzPpa6atPxoPBlIHGCa0zRBK2EZt165622Xe7Wc"

payload = {
    "statement": "MATCH (n) RETURN n LIMIT 5"
}

response = requests.post(
    URL,
    auth=HTTPBasicAuth(USER, PASSWORD),
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
    },
    data=json.dumps(payload)
)

if response.status_code in (200, 202):
    print("✅ Query berhasil!")
    print(json.dumps(response.json(), indent=2))
else:
    print("❌ Query gagal")
    print(response.status_code, response.text)
