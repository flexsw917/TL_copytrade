from tradelocker import TLAPI
import requests

# Define your credentials
environment = "https://live.tradelocker.com"
username = "username"
password = "psswrd"
server = "server"

# Initialize the API client
tl = TLAPI(environment=environment, username=username, password=password, server=server)

# Function to obtain JWT token
def get_jwt_token(username, password, server):
    url = f"{environment}/backend-api/auth/jwt/token"
    payload = {
        "email": username,
        "password": password,
        "server": server
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 201:
        data = response.json()
        return data['accessToken'], data['refreshToken']
    else:
        raise Exception("Failed to obtain JWT token")

# Get the JWT token
access_token, refresh_token = get_jwt_token(username, password, server)
print("Access Token:", access_token)
print("Refresh Token:", refresh_token)
