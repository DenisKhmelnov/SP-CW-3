import json


def get_posts_all():
    """
    :return: Возвращает все посты
    """
    with open("data_storage/data.json", encoding="utf-8") as file:
        posts_list = json.load(file)
        return [parse_hash_tag(post) for post in posts_list]



def get_posts_by_user(user_name) -> list[dict]:
    """
    :param user_name: имя пользователя
    :return: возвращает список постов от заданного пользователя
    """
    posts = get_posts_all()
    user_posts = [post for post in posts if post["poster_name"] == user_name]
    return user_posts


def get_comments_by_post_id(post_id) -> list[dict]:
    """
    :param post_id: номер поста
    :return: лист с комментариями, которые написаны к искомому посту с заданным номером
    """
    with open("data_storage/comments.json", encoding="utf-8") as file:
        all_comments = json.load(file)

    post_comments = [comment for comment in all_comments if comment["post_id"] == post_id]
    return post_comments


def search_for_posts(query) -> list[dict]:
    """
    :param query: искомая подстрока в посте
    :return: список постов, где в тексте встречается искомая подстрока
    """
    posts = get_posts_all()
    matched_posts = [post for post in posts if query.lower() in post["content"].lower()]
    return matched_posts


def get_post_by_pk(pk) -> dict:
    """
    :param pk: уникальный номер поста
    :return: возвращает один пост с искомым уникальным номером
    """
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == pk:
            return post


def parse_hash_tag(post: dict):
    """
    :param post:
    :return: возвращает пост, где хэштеги заменены на html ссылку
    """
    words_list = post["content"].split(" ")
    parsed_content = []
    for word in words_list:
        if word.startswith("#"):
            html_replacement = f'<a href="/tag/{word[1:]}">{word}</a>'
            parsed_content.append(html_replacement)
        else:
            parsed_content.append(word)
    post["content"] = " ".join(parsed_content)
    return post


def get_posts_by_tag(tag):
    """
    :param tag:
    :return: возвращает посты, в которых встречается искомый тэг
    """
    tagged_posts=[]
    posts = get_posts_all()
    for post in posts:
        if tag in post["content"]:
            tagged_posts.append(post)
    return tagged_posts