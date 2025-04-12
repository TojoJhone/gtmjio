import requests

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

    # Debugging: Print the first few lines to inspect structure
    print("First few lines of the playlist:")
    print("\n".join(lines[:10]))  # Print the first 10 lines to inspect

    for i in range(len(lines)):
        line = lines[i]
        if line.startswith("#EXTINF"):
            print(f"Checking channel: {line}")  # Debugging: Print the current channel info

            # Check if the line contains any of the desired channel names
            keep = any(channel in line for channel in CHANNELS_TO_KEEP)
        if keep:
            filtered.append(line)

    # Debugging: Show filtered lines
    print("\nFiltered channels:")
    print("\n".join(filtered[:10]))  # Print the first 10 filtered lines

    with open("custom_playlist.m3u", "w", encoding="utf-8") as f:
        f.write("\n".join(filtered))

if __name__ == "__main__":
    filter_playlist()
