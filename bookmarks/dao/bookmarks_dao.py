import json
from utils import get_posts_all


def get_bookmarks() -> list[int]:
    with open("./data_storage/bookmarks.json", encoding="utf-8") as file:
        return json.load(file)


def add_bookmark(new_bookmark):
    bookmarks = get_bookmarks()
    with open("./data_storage/bookmarks.json", "w", encoding="utf-8") as file:
        if new_bookmark not in bookmarks:
            bookmarks.append(new_bookmark)
        json.dump(bookmarks, file)


def delete_bookmark(bookmark: int):
    bookmarks = get_bookmarks()
    with open("./data_storage/bookmarks.json", "w", encoding="utf-8") as file:
        if bookmark in bookmarks:
            bookmarks.remove(bookmark)
        json.dump(bookmarks, file)


def load_bookmarks_posts() -> list[dict]:
    bookmark_posts = []
    bookmarks = get_bookmarks()
    posts = get_posts_all()
    for post in posts:
        if post["pk"] in bookmarks:
            bookmark_posts.append(post)
    return bookmark_posts
