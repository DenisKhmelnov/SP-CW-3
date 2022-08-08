import pytest
import utils


def test_get_posts_all():
    assert len(utils.get_posts_all()) == 8


def test_get_posts_by_user():
    assert len(utils.get_posts_by_user("hank")) == 2


def test_get_comments_by_post_id():
    assert len(utils.get_comments_by_post_id(1)) == 4


def test_search_for_posts():
    assert len(utils.search_for_posts("ром")) == 2
