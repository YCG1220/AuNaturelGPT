# Import the requests library
import requests

# Set the API endpoint and parameters
url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'key': 'YOUR_API_KEY',
    'cx': 'YOUR_SEARCH_ENGINE_ID',
    'q': 'test'
}

# Make a test request to the API
response = requests.get(url, params=params)

# Verify that we receive a valid response
if response.status_code == 200:
    print('Connected to Google Custom Search API')
else:
    print('Failed to connect to Google Custom Search API')
