import os
import requests

mobilenodes_dir = os.path.dirname(os.path.abspath(os.path.join(__file__, '..')))

url = "http://localhost:49167/GetSettings"

# Replace with your actual file path
file_path = os.path.join(mobilenodes_dir, "token.txt")

# Open the file and read its contents
with open(file_path, "r") as file:
    user_token = file.read()

# Make the GET request
response = requests.get(url, params={"userToken": user_token})

# Check the response
if response.status_code == 200:
    # If the request was successful, print the settings
    print(response.json())
else:
    # If the request failed, print the status code
    print(f"Request failed with status code {response.status_code}")
