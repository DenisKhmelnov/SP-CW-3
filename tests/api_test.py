from app import app

keys_list = ["poster_name",
             "poster_avatar",
             "pic",
             "content",
             "views_count",
             "likes_count",
             "pk"]


def test_api_all_posts():
    response = app.test_client().get("/api/posts")
    # проверяем, что возвращается верный статус код
    assert response.status_code == 200
    # проверяем, что возвращается лист с постами
    assert type(response.json) == list
    # проверяем ключи в посте
    for post in response.json:
        for key in keys_list:
            assert key in post.keys(), f"Нет ключа {key} в посте {post['pk']}"


def test_api_single_post():
    response = app.test_client().get("/api/posts/1")
    # проверяем, что возвращается верный статус код
    assert response.status_code == 200
    # проверяем, что возвращается лист с постами
    assert type(response.json) == dict
    # проверяем ключи в посте
    for key in keys_list:
        assert key in response.json.keys(), f"Нет ключа {key}"
