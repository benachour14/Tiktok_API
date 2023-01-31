import requests

# profile = "https://www.tiktok.com/@anassbenachour4"
profile = "https://www.tiktok.com/@anassbenachour4/video/7191758513624976646"


url = f"https://www.tiktok.com/oembed?url={profile}"

response  = requests.get(url)

resp = response.json()
music_name_start = resp['html'].rfind('♬') 
string = resp['html'][music_name_start:]
music_name_end = string.rfind('</a>') + music_name_start
print(resp['html'][music_name_start:music_name_end])
