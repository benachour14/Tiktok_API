import requests

# url= "https://v16-webapp.tiktok.com/548830605cd710c8c1d7f7d18b194765/63d170d5/video/tos/useast2a/tos-useast2a-pve-0068/osbkhk5JzBBeSfsQgoPyDCAFwXIQKjRjnERcDu/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2658&bt=1329&cs=0&ds=3&ft=-Elcom.MPD12NsoPh8-UxItFhYKt3wv25IcAV&mime_type=video_mp4&qs=0&rc=Ojk2OTw2N2k5PDQ5ZTlpZkBpM3I3djQ6Zmg3aTMzNzczM0BfNTEuMGJiNi8xLS8tLWFhYSNfY2FpcjRfMTRgLS1kMTZzcw%3D%3D&l=202301251211233C5BA86FB25E3FBD79D2&btag=80000&__vid=TT-vCache-7191758513624976646"
url = "https://v16-webapp.tiktok.com/7c78a566ff41bd0cd01f2f28b1d12503/63d17403/video/tos/useast2a/tos-useast2a-pve-0068/oUvobnQAfDsduBkjA4HSUhIObWEXEBBJbnDRze/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=3370&bt=1685&cs=0&ds=3&ft=-Elcom.MPD12NEbPh8-Ux~TFhYKt3wv25VcAV&mime_type=video_mp4&qs=0&rc=aTk0MzpoMzRnZDU8ZWhnZ0BpM3V4bjQ6ZmU7aTMzNzczM0AxMDQuY2M0Xy4xLi4xYmEuYSNwYmdvcjRvXzRgLS1kMTZzcw%3D%3D&l=2023012512250352FEBE334087C1B84206&btag=80000&__vid=TT-vCache-7191832630340406533"

response = requests.get(url)
print(response)

video_data = response.content

with open("video_2.mp4", "wb") as f:
    f.write(video_data)

