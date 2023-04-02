from src.channel import Channel
import pytest


@pytest.fixture()
def expl1():
    return Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')


@pytest.fixture()
def expl2():
    return Channel('UC1eFXmJNkjITxPFWTy6RsWg')


def test_channel_init(expl1):
    assert expl1.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'


def test_print_info(expl1):
    assert expl1.channel_id == 'UCMCgOm8GZkHp8zJ6l7_hIuA'
    assert expl1.title == 'вДудь'


def test_to_json():
    vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
    assert vdud.to_json('vdud.json') == None


def test_add(expl1, expl2):
    assert expl1 + expl2 <= 14010000


def test_sub(expl1, expl2):
    assert expl1 - expl2 <= 6590000 or expl1 - expl2 >= 6590000


def test_ge(expl1, expl2):
    assert expl1 >= expl2
