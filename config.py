# Configuration file for API keys and settings
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the API keys from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
gfw_api_key = os.getenv("GFW_API_KEY")
