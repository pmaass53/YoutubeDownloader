import scrapetube
import os
videos = scrapetube.get_channel("UCvt0HYxX34vUvqu66HLXeUw")
all = []

for video in videos:
    all.append(video["videoId"])

print("loaded " + str(len(all)) + " videos")

# reset watched videos
#with open("downloaded", "w") as f:
#    f.writelines(id + "\n" for id in ids)
watched = []
with open("downloaded", "r") as f:
    for line in f.readlines():
        watched.append(line.strip())
        #print(watched[-1])

toDownload = []
for item in all:
    if item not in watched:
        toDownload.append(item)
print("to download " + str(len(toDownload)) + " videos")

for videoId in toDownload:
    print("downloading " + videoId)
    os.system('./yt-dlp https://www.youtube.com/watch?v=' + videoId + ' -o "downloads/%(title)s.%(ext)s"')
    with open("downloaded", "a") as f:
        f.write(videoId + "\n")