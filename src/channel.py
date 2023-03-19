import os
from googleapiclient.discovery import build

class Channel:

    """Класс для ютуб-канала"""
    api_key: str = os.getenv('API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
        channel = Channel.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(channel)