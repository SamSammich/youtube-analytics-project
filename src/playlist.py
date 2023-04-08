import os

from googleapiclient.discovery import build

class PlayList:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.video_info = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                     id=playlist_id).execute()
        self.video_title = self.video_info["items"][0]["snippet"]['title']
        self.video_url = "https://www.youtube.com/channel/" + f"{playlist_id}"
        self.video_view = self.video_info['items'][0]['statistics']['viewCount']
        self.video_like = self.video_info['items'][0]['statistics']['likeCount']
        self.video_comment = self.video_info['items'][0]['statistics']['commentCount']

    def total_duration(self):
        pass

    def show_best_video(self):
        pass
