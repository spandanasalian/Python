from pytube import YouTube
yt=YouTube("https://www.youtube.com/watch?v=ET9zvLo87mY")
dw=yt.streams.first()
dw.download("D:\downloadpythonvideo")