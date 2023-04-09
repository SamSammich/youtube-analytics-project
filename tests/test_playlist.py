import datetime
from src.playlist import PlayList
import pytest


@pytest.fixture()
def exp():
    return PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')


def test_init(exp):
    assert exp.title == "Редакция. АнтиТревел"
    assert exp.url == "https://www.youtube.com/playlist?list=PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb"


def test_total_duration(exp):
    duration = exp.total_duration
    assert str(duration) == "3:41:01"
    assert isinstance(duration, datetime.timedelta)
    assert duration.total_seconds() == 13261.0


def test_show_best_video(exp):
    assert exp.show_best_video() == "https://youtu.be/9Bv2zltQKQA"
