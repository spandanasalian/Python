from pytube import YouTube
video_list=open("download.txt","r")

for i in video_list:
    yt=YouTube(i)
#first() takes the highest resolution of the video
    dw=yt.streams.first()
    dw.download("D:\downloadpythonvideo")
    print("downloaded",i)
