import requests

# Your API key
api_key = '66c73004-f5bd-496e-a158-78a04de8f521'  # Make sure the API key is in quotes

# Set the URL for the GFW Deforestation endpoint
url = 'https://data-api.globalforestwatch.org/v1/deforestation?country=BRA&start=2001&end=2020&format=json'

# Set headers with your API key
headers = {
    'x-api-key': '66c73004-f5bd-496e-a158-78a04de8f521'  # Use the variable with quotes
}

# Make the GET request to the API
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print(data)  # Do something with the data
else:
    print(f'Error: {response.status_code} - {response.text}')
