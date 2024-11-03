import requests

# Your auth token
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3MjUyZmYyNTlhMzhlYmRiMTY4ZjViNCIsInJvbGUiOiJVU0VSIiwicHJvdmlkZXIiOiJsb2NhbCIsImVtYWlsIjoieWFzbWluamFpbjA0QGdtYWlsLmNvbSIsImV4dHJhVXNlckRhdGEiOnsiYXBwcyI6WyJnZnciXX0sImNyZWF0ZWRBdCI6MTczMDQ5MDc3MzY3NiwiaWF0IjoxNzMwNDkwNzczfQ.jMFJ_3k9pGB_Y9NWKVG0SRyTxwXWAdw4Ii__DgeKw5c"  # Replace with your actual token

# Set the endpoint for creating an API key
url = "https://data-api.globalforestwatch.org/auth/apikey"

# Define the payload with your application details
payload = {
    "alias": "api-key-for-new-app",
    "email": "yasminjain04@gmail.com",  # Replace with your email
    "organization": "Madhav institute",  # Replace with your organization name
    "domains": []  # Specify any domains if needed
}

# Set the headers
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Content-Type": "application/json"
}

# Make the POST request
response = requests.post(url, headers=headers, json=payload)

# Check the response
if response.status_code == 200:
    api_key = response.json().get("data")[0].get("api_key")
    print("Your API Key:", api_key)
else:
    print("Error:", response.status_code, response.json())
