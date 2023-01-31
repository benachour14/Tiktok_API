import sys
import requests
import os

if len(sys.argv) < 2:
    print("passez le refresh_token en paramétres")
    os._exit(os.EX_OK)

client_id = "awi1zy45ku8ss868"
token_data = {
'grant_type': 'refresh_token',
'refresh_token': sys.argv[1],
'client_key': client_id,
}   

response = requests.post('https://open-api.tiktok.com/oauth/refresh_token/', data=token_data)
token_response = response.json()
if token_response['data']['error_code'] == 10010:
    print("refresh_token expiré / invalide")
else:
    print(token_response['data']['access_token'])
