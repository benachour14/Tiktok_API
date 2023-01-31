import sys
import os
import requests

if len(sys.argv) < 3:
    print("passez l'access token et le cursor")
    os._exit(os.EX_OK)

endpoint = 'https://open.tiktokapis.com/v2/video/list/?fields=id,create_time,share_url,title,video_description,duration,cover_image_url,embed_link,like_count,comment_count,share_count,view_count'
access_token = sys.argv[1]
cursor = sys.argv[2]

headers = {'Authorization': f'Bearer {access_token}',
            "Content-Type": "application/json"
           }
data = {
    "cursor": cursor,
    'max_count': 1
}

# Make the GET request
response = requests.post(endpoint, headers=headers, json=data)
videos = response.json()
print(videos)


if videos['error']['code'] == 'access_token_invalid':
    print("access token invalide")
    os._exit(os.EX_OK)
elif videos['error']['code'] == 'Access_token expired, please refresh or re-authorize.':
    print('access token expiré')
    os._exit(os.EX_OK)

print(len(videos['data']['videos']))
for video in videos['data']['videos']:
    print(f"id de la video  : {video['id']}")
    print(f"lien de la video : {video['share_url']}")
    print(f"date de creation de la video : {video['create_time']}")
    print(f"titre de la video : {video['title']}")
    print(f"description de la video : {video['video_description']}")
    print(f"durée de la video : {video['duration']}")
    print(f"nombre de like : {video['like_count']}")
    print(f"nombre de commentaires : {video['comment_count']}")
    print(f"nombre de partage : {video['share_count']}")
    print(f"nombre de video : {video['view_count']}")
    print(f"lien vers l'image de cover de la video : {video['cover_image_url']}")
    print("fin")
    print('===================')
print('has more video :', videos['data']['has_more'], videos['data']['cursor'])

