import requests
import sys
import os

if len(sys.argv) < 2:
    print("passez le code d'autorization en paramétres")
    os._exit(os.EX_OK)

client_id = 'awi1zy45ku8ss868'
client_secret = 'ae165492823db6531b132ae057b141f0'
token_data = {
    'grant_type': 'authorization_code',
    'code': sys.argv[1],
    'client_key': client_id,
    'client_secret': client_secret,
}

response = requests.post('https://open-api.tiktok.com/oauth/access_token/', data=token_data)

# Extract the access token and refresh token from the response
token_response = response.json()

if token_response['data']['error_code'] == 10007:
    print("code d'autorisation invalid / expiré")
else:
    print(token_response['data']['refresh_token'])

