from flask import Blueprint, render_template, request
import utils

main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")


@main_blueprint.route("/")
def page_index():
    """
    :return: главная страница со всеми постами
    """
    posts = utils.get_posts_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/posts/<int:postid>/")
def page_post(postid):
    """
    :param postid: уникальный номер поста
    :return: представление для поста с искомым id
    """
    post = utils.get_post_by_pk(postid)
    comments = utils.get_comments_by_post_id(postid)
    return render_template("post.html", post=post, comments=comments, comments_count=len(comments))


@main_blueprint.route("/search/")
def page_search():
    """
    :return: возвращает первые 10 постов в которых встречается искомая подстрока
    """
    subs = request.args.get("s")
    matched_posts = utils.search_for_posts(subs)[:10]
    return render_template("search.html", posts=matched_posts, posts_count=len(matched_posts))


@main_blueprint.route("/users/<username>")
def page_user(username):
    user_posts = utils.get_posts_by_user(username)
    return render_template("user-feed.html", posts=user_posts)


@main_blueprint.route("/tag/<tagname>")
def show_tag_page(tagname):
    tag = f"#{tagname}"
    tagged_posts = utils.get_posts_by_tag(tag)
    return render_template("tag.html", posts=tagged_posts, tag=tag)
