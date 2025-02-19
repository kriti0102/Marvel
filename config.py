import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path=".env", override=True)

# Marvel API Keys from environment variables
PUBLIC_KEY = os.getenv("MARVEL_PUBLIC_KEY")
PRIVATE_KEY = os.getenv("MARVEL_PRIVATE_KEY")

API_URL = "https://gateway.marvel.com:443/v1/public/characters"
TOTAL_RECORDS = 1564  # Total available Marvel characters
LIMIT = 100  # API limit per request
CSV_FILENAME = "marvel_characters.csv"
MAX_WORKERS = 5  # Number of parallel API requests