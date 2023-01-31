import sys
import requests
import os 

if len(sys.argv) < 2:
    print("passez l'access_token en paramétres")
    os._exit(os.EX_OK)
    
endpoint = 'https://open.tiktokapis.com/v2/user/info/?fields=open_id,union_id,avatar_url,display_name,bio_description,profile_deep_link,is_verified,follower_count,following_count,likes_count'
access_token = sys.argv[1]

headers = {
    'Authorization': f'Bearer {access_token}'
}

# Make the GET request
response = requests.get(endpoint, headers=headers)
user = response.json()
if user['error']['code'] == 'access_token_invalid':
    print("access token invalide")
    os._exit(os.EX_OK)
elif user['error']['code'] == 'Access_token expired, please refresh or re-authorize.':
    print('access token expiré')
    os._exit(os.EX_OK)
    
user_info = user['data']['user']

print(f"l'id du l'utilisateur sur l'app : {user_info['open_id']}")
print(f"image de profil du l'utilisateur : {user_info['avatar_url']}")
print(f"nom du profil de l'utilisateur : {user_info['display_name']}")
print(f"Bio de l'utilisateur: {user_info['bio_description']}")
print(f"lien de la page tiktok de l'utilisateur : {user_info['profile_deep_link']}")
print(f"nombre d'abonnées de l'utilisateur : {user_info['follower_count']}")
print(f"nombre des pages suivi par l'utilisateur : {user_info['following_count']}")
print(f"nombre de likes recus  : {user_info['likes_count']}")


profile = user_info['display_name']


url = f"https://www.tiktok.com/oembed?url=https://www.tiktok.com/@{profile}"

response  = requests.get(url)
if response.status_code == 400:
    print("private account")
else:
    print("Public account")








