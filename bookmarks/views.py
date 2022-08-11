from flask import Blueprint, redirect, render_template
from bookmarks.dao.bookmarks_dao import load_bookmarks_posts, add_bookmark, delete_bookmark

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder="templates")


@bookmarks_blueprint.route("/bookmarks/add/<int:postid>")
def save_bookmark(postid):
    add_bookmark(postid)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/remove/<int:postid>")
def remove_bookmark(postid):
    delete_bookmark(postid)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks")
def show_bookmarks():
    posts = load_bookmarks_posts()
    return render_template("bookmarks.html", posts=posts)
