import json
import certifi
import urllib.request
import urllib.parse
import ssl
import time
import logging
import csv
from concurrent.futures import ThreadPoolExecutor
from config import PUBLIC_KEY, PRIVATE_KEY, API_URL, TOTAL_RECORDS, LIMIT, CSV_FILENAME, MAX_WORKERS
from utils import generate_hash

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def fetch_characters_batch(offset: int) -> list:
    """
    Fetch a batch of Marvel characters from the API.
    
    :param offset: Offset value for pagination
    :return: List of character data (name, number of comics)
    """
    ts = str(int(time.time()))  # Generate timestamp
    hash_value = generate_hash(ts, PRIVATE_KEY, PUBLIC_KEY)
    
    # Prepare API request parameters
    params = {
        'apikey': PUBLIC_KEY,
        'ts': ts,
        'hash': hash_value,
        'orderBy': 'name',
        'limit': LIMIT,
        'offset': offset
    }
    request_url = f"{API_URL}?{urllib.parse.urlencode(params)}"
    
    # Create an SSL context with certifi's CA bundle
    ctx = ssl.create_default_context(cafile=certifi.where())
    ctx.set_ciphers('DEFAULT@SECLEVEL=1')
    
    try:
        with urllib.request.urlopen(request_url, context=ctx) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            # Extract character data
            return [(char['name'], char['comics']['available']) for char in data.get('data', {}).get('results', [])]
    except Exception as e:
        logging.error(f"Error fetching offset {offset}: {e}")
        return []

def fetch_marvel_characters():
    """
    Fetch Marvel character data in parallel and save results to a CSV file.
    """
    logging.info("Starting parallel character data extraction...")
    
    # Open CSV file for writing
    with open(CSV_FILENAME, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Character Name', 'Quantity of Comics they appear in'])  # Write CSV header
        
        offsets = range(0, TOTAL_RECORDS, LIMIT)
        
        # Use ThreadPoolExecutor to fetch characters in parallel
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            results = executor.map(fetch_characters_batch, offsets)
        
        # Write results to CSV
        for batch in results:
            writer.writerows(batch)
        
    logging.info("Character data extraction completed successfully!")
