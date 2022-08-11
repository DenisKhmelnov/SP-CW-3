from flask import Flask, jsonify
from main.views import main_blueprint
from bookmarks.views import bookmarks_blueprint
from logs.log import logger_api
import utils


app = Flask(__name__)

#конфиги для корректного отображения JSON
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


app.register_blueprint(main_blueprint)
app.register_blueprint(bookmarks_blueprint)


## Обработчики ошибок

@app.errorhandler(404)
def not_found(e):
    return "Такой страницы не существует, проверьте правильность URL", 404

@app.errorhandler(500)
def server_error(e):
    return "Internal Server Error", 500


#API

@app.route("/api/posts")
def all_posts():
    """
    :return: возвращает json со всеми постами
    """
    logger_api.info("Запрошен /api/posts")
    posts = utils.get_posts_all()
    return jsonify(posts)

@app.route("/api/posts/<int:post_id>")
def single_post(post_id):
    """
    :param post_id:
    :return: возвращает искомый пост в формате json
    """
    logger_api.info(f"Запрошен /api/posts/{post_id}")
    post = utils.get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == '__main__':
    app.run()
