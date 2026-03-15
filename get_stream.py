import requests
import re

url = "https://www.alphacyprus.com.cy/live"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(url, headers=headers)

match = re.search(r'https://l4\.cloudskep\.com/[^"]+\.m3u8\?wmsAuthSign=[^"]+', r.text)

if match:
    stream = match.group(0)

    playlist = f"""#EXTM3U
#EXTINF:-1,Alpha Cyprus
{stream}
"""

    with open("alpha.m3u8", "w") as f:
        f.write(playlist)

    print("Playlist gemaakt")
else:
    print("Stream niet gevonden")
