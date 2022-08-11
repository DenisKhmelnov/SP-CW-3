from flask import Blueprint, redirect
from bookmarks.dao.bookmarks_dao import add_bookmark, delete_bookmark

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder="templates")


@bookmarks_blueprint.route("/bookmarks/add/<int:postid>")
def save_bookmark(postid):
    add_bookmark(postid)
    return redirect("/", code=302)


@bookmarks_blueprint.route("/bookmarks/remove/<int:postid>")
def remove_bookmark(postid):
    delete_bookmark(postid)
    return redirect("/", code=302)
