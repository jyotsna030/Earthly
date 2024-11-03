import requests

url = "https://data-api.globalforestwatch.org/auth/token"
payload = {
    "username": "Yasmine",  # replace with your username
    "password": "Jyo@0306"     # replace with your password
}

response = requests.post(url, data=payload)

# Check if the request was successful
if response.status_code == 200:
    auth_token = response.json()['data']['access_token']
    print("Your Auth Token:", auth_token)
else:
    print("Failed to get auth token:", response.json())
