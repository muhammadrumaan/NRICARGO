import requests
import json

from django.conf import settings  # Import settings for CSRF cookie name


# Define the URL of your Django application endpoint
url = 'http://127.0.0.1:8000/cart/'

# Define the dictionary of products and quantities
products_info = {
    'Spices': 2,
    'Saree': 1,
    # Add more products as needed
}

# Convert the products_info dictionary to JSON format
payload = json.dumps(products_info)

# Get the CSRF cookie value from your session (assuming you have a session established)
# Replace this with your session method depending on your setup
csrf_token = ""  # Get the CSRF token from your session or API endpoint

# Set the headers with the CSRF token
headers = {'X-CSRFToken': csrf_token}

# Send the POST request with JSON payload and headers
response = requests.post(url, headers=headers, json=payload)

# Print the response
print(response.text)
