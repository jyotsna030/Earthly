import requests
from config import openai_api_key, gfw_api_key

def generate_art(theme):
    """Generate eco-art based on the theme."""
    prompt = f"Create a visually impactful art piece showing the effects of {theme} on the environment."
    headers = {"Authorization": f"Bearer {openai_api_key}"}
    response = requests.post(
        "https://api.openai.com/v1/images/generations", 
        headers=headers, 
        json={"prompt": prompt, "n": 1, "size": "512x512"}
    )
    
    if response.status_code == 200:
        image_url = response.json().get("data")[0]["url"]
        return image_url
    else:
        return None  # Error handling should be improved in production

def fetch_datasets(page_number=1, page_size=5):
    """Fetch datasets from Global Forest Watch."""
    endpoint = "https://data-api.globalforestwatch.org/datasets"
    headers = {
        'Authorization': f'Bearer {gfw_api_key}',
        'Content-Type': 'application/json'
    }
    params = {
        'page[number]': page_number,
        'page[size]': page_size
    }
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        return []  # Error handling should be improved in production
