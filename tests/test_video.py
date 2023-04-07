from src.video import Video, PLVideo
import pytest


@pytest.fixture()
def video():
    return Video('9lO06Zxhu88')


def test_video_init(video):
    assert video.video_id == '9lO06Zxhu88'

def test_video_str(video):
    video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
    assert str(video) == 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
    assert str(video2) == 'Пушкин: наше все?'