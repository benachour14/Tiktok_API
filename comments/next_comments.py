import requests
import sys 

url = "https://www.tiktok.com/api/comment/list/?aid=1988&app_language=ja-JP&app_name=tiktok_web&aweme_id=7191758513624976646&battery_info=0.82&browser_language=fr-FR&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F109.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&count=20&current_region=JP&cursor=0&device_id=7183973066913285637&device_platform=web_pc&focus_state=true&fromWeb=1&from_page=video&history_len=5&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=FR&referer=https%3A%2F%2Fwww.tiktok.com%2F%40anassbenachour4%2Fvideo%2F7191758513624976646&region=FR&root_referer=https%3A%2F%2Fwww.tiktok.com%2F%40anassbenachour4%2Fvideo%2F7191758513624976646&screen_height=864&screen_width=1536&tz_name=Africa%2FCasablanca&verifyFp=verify_ld8y9ouw_Npb1AZEw_GshL_4rNv_88vs_xexGt9TBPNzj&webcast_language=fr&msToken=z9f57-9rUlHxZasdDVqQ6NTIt3n5RbM8HTRZO-MayknVcXXLerkTlUstDlSExQW2_NV2PdKRVoXPYyo5BJZ9elNpb8T0JL_TDKeM8FADieUddwAoXTlMeFwNyou6q7oAZYWa_N8=&X-Bogus=DFSzswVOqpkAN9ILS43Mn5YklTIn&_signature=_02B4Z6wo00001HzOlnQAAIDBorjO0vFv43x8zpLAAHzr12"

headers = {
        "Content-Type": "application/json",
        "Cache-Control" : "max-age=0, no-cache, no-store",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "cookie": "_abck=CD289641104442F8350DC9BC6761EDAA~-1~YAAQNltDUK19xMuFAQAAK/1i3wnJ32RhSzXg0qyVOcdRv3tCO4+hPIKQzc2kHD6jAIGPXlnJiMNAAhkLHa86gIwhZsiwxSfKNVFq7zSaVlnt4IT30vy4qfrru77wCqbpA2IiNaGkw6NgF8sRki/kuNzMLZGx96+PZb2iBq0Fubs6ivLKQWgiLDZ0MW/vKBhMB2yB8wuWMY3JhBbQAalgZvUyIDtu3abn8QTgZizawtLoAcEX/8kmOHflbi3J07yyWL/9G8cQ+CWr5yjGlsE6UR5Zk74uaG+kaOd/9qA9suTvxnEpBsppXskMMA8MfenKSS9+znT03un+metrAb/AHWv6Eg5fkW50nweKlSTYfm06w/h3H6N7uB3GZ5YG+Bw=~-1~-1~-1; Domain=.tiktok.com; Path=/; Expires=Tue, 23 Jan 2024 16:08:04 GMT; Max-Age=31536000; Secure",
        "Connection": "keep-alive",
        "referer" : "https://www.tiktok.com/@anassbenachour4/video/7191758513624976646",
        }

response = requests.get(url, headers=headers)
resp = response.json()
print(resp)
# for i in range(len(resp['comments'])):
#     print(resp['comments'][i]['text'])
