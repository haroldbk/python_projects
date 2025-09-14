from googleapiclient.discovery import build
import convertVideo

api_key ="AIzaSyBKo0Ewn5pi9Yeiudwa5qbU9aFnKyEJaNc"

youtube = build("youtube", "v3", developerKey=api_key)

response=youtube.search().list(
    q='carolina shag boogie walk ',
    part='snippet',
    type='video',
    maxResults=5
).execute()
#print(response)
for item in response['items']:
    title = item['snippet']['title']
    video_id=item['id']['videoId']
    url=f'https://www.youtube.com/watch?v={video_id}'
    print(f'{title}-{url}')
    convertVideo.convertVideo(url, f'{title}.mp4')
