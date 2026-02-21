import requests
import json
import os

BRAVE_API_KEY = "BSATNM2NylbIg_iuDTP9YvrKcIrbxew"
query = "events in Tampa tonight February 20 2026"

url = "https://api.search.brave.com/res/v1/web/search"
headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip",
    "X-Subscription-Token": BRAVE_API_KEY
}
params = {"q": query}

try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    
    # Print top results
    for i, result in enumerate(data.get('web', {}).get('results', [])[:5]):
        print(f"[{i+1}] {result['title']}")
        print(f"    {result['url']}")
        print(f"    {result['description'][:200]}...")
        print()
        
except Exception as e:
    print(f"Error: {e}")
