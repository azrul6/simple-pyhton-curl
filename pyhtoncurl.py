import requests

url = "https://api.example.com/data"  # Replace with the desired URL

response = requests.get(url)

if response.status_code == 200:
    # Request successful
    data = response.json()  # Get the response data in JSON format
    print(data)
else:
    # Request failed
    print("Request failed with status code:", response.status_code)
