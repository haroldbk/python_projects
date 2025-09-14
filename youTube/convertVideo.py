from pytubefix import YouTube

def convertVideo(url,fname):
   
   # video_url ='https://youtu.be/mv0NftolNgk'
    video_url = url

    #create a youtube object
    yt=YouTube(video_url)

    #get the highest resolution stream (mp4 by default)
    video_stream = yt.streams.filter(file_extension='mp4',progressive=True).get_highest_resolution()

    video_stream.download(output_path=r'C:\Users\haroldbk\OneDrive\Dance_demos\shag' ,filename=fname)

    print('Download complete')

convertVideo('https://www.youtube.com/watch?v=dsCl2kXJca4', 'what_a_feeling.mp4')    