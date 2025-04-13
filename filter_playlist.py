import requests

SOURCE_URL = "https://raw.githubusercontent.com/Esmaeli/m3u/refs/heads/main/mvp.m3u"
CHANNELS_TO_KEEP = ["zee cinema", "star gold", "pictures hd", "hindi"]

def filter_playlist():
    response = requests.get(SOURCE_URL)
    lines = response.text.splitlines()
    
    filtered = ["#EXTM3U"]
    keep = False
    
    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("#EXTINF"):
            keep = any(channel.lower() in line.lower() for channel in CHANNELS_TO_KEEP)
        if keep:
            filtered.append(line)

    with open("custom_playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(filtered))

if __name__ == "__main__":
    filter_playlist()
