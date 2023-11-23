# Use POST as there is no limit to characters like GET

import requests
import json

url = "http://localhost:8000/ask"

payload = json.dumps({
  "question": "Q: What are the names of the days of the week?"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)