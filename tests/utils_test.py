import pytest
from utils import get_posts_all, get_posts_by_user, get_post_by_pk


def test_post_all():
    assert len(get_posts_all()) == 8


def test_post_by_user():
    assert get_posts_by_user('leo')['pk'] == 1


def test_post_by_pk():
    assert get_post_by_pk(1)['poster_name'] == 'leo'


