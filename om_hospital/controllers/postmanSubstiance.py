import requests
import json

url = 'http://hgagy-latitude-e5570:8014/api/test'
data = {
    'id':"20",
    'doctor_name': 'hhhgagy',
    'age': "1000",
    'gender': "male"
}

# Send POST request with JSON data
response = requests.post(url, json=data)

print(response.text)  # Print the response from the server
