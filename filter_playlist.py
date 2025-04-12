import requests
import re

SOURCE_URL = "https://raw.githubusercontent.com/Esmaeli/m3u/refs/heads/main/mvp.m3u"

# ✅ Exact names of channels to keep
CHANNELS_TO_KEEP = [
    "Zee Tv HD",
    "&TV HD",
    "Zee Cinema HD",
    "Zee Action",
    "Zee Bollywood",
    "Zee Classic",
    "& Pictures HD",
    "&Flix HD",
    "Star Gold HD",
    "Star Bharat HD",
    "Star Gold 2",
    "Star Utsav Movies",
    "Star Plus HD",
    "Star Romance",
    "Star Gold Thrills"
]

def filter_playlist():
    response = requests.get(SOURCE_URL)
    lines = response.text.splitlines()

    filtered = ["#EXTM3U"]
    keep = False

    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("#EXTINF"):
            # Extract the display name from EXTINF line using regex
            match = re.search(r'tvg-name="([^"]+)"', line)
            if match:
                channel_name = match.group(1).strip()
                keep = channel_name in CHANNELS_TO_KEEP
            else:
                keep = False
        if keep:
            filtered.append(line)

    with open("custom_playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(filtered))

if __name__ == "__main__":
    filter_playlist()
