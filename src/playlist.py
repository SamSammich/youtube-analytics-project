import datetime
import os
import isodate
from googleapiclient.discovery import build


class PlayList:
    API_KEY: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    def __init__(self, playlist_id):
        self.__playlist_id = playlist_id
        self.__playlists_info = self.youtube.playlists().list(id=playlist_id, part='contentDetails,snippet',
                                                                maxResults=50, ).execute()

        self.__each_video_info = self.youtube.playlistItems().list(playlistId=self.__playlist_id,
                                                                     part='contentDetails', maxResults=50, ).execute()
        self.__video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.__each_video_info['items']]

        self.__video_response = self.youtube.videos().list(part='contentDetails, statistics', id=','.join(
            self.__video_ids)).execute()

        self.__title = self.__playlists_info['items'][0]['snippet']['title']
        self.__url = f"https://www.youtube.com/playlist?list={self.__playlist_id}"

    @property
    def url(self):
        """Returning url"""
        return self.__url

    @property
    def title(self):
        """Returning title"""
        return self.__title

    @property
    def total_duration(self):
        """Finding total duration"""
        total_duration = datetime.timedelta()

        for video in self.__video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += duration
        return total_duration

    def show_best_video(self):
        """Finding best video """
        max_like = 0
        best_video = None
        for i in range(len(self.__video_response['items'])):
            like_count = int(self.__video_response['items'][i]['statistics']['likeCount'])
            if like_count > max_like:
                max_like = like_count
                best_video = self.__video_response['items'][i]['id']
        return f"https://youtu.be/{best_video}"



pl = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(pl.show_best_video())
