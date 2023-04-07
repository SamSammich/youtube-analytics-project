import os

from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id):
        self.__video_id = video_id
        self.video_info = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                     id=video_id).execute()
        self.video_title = self.video_info["items"][0]["snippet"]['title']
        self.video_url = "https://www.youtube.com/channel/" + f"{video_id}"
        self.video_view = self.video_info['items'][0]['statistics']['viewCount']
        self.video_like = self.video_info['items'][0]['statistics']['likeCount']
        self.video_comment = self.video_info['items'][0]['statistics']['commentCount']

    def __str__(self):
        """Returning Video Title """
        return self.video_title

    @property
    def video_id(self):
        return self.__video_id


class PLVideo(Video):
    def __init__(self, video_id,  playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return self.video_title
