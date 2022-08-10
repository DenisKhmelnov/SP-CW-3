from flask import Flask, jsonify

import utils
from main.views import main_blueprint

app = Flask(__name__)

#конфиги для корректного отображения JSON
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


app.register_blueprint(main_blueprint)



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
    posts = utils.get_posts_all()
    return jsonify(posts)

@app.route("/api/posts/<int:post_id>")
def single_post(post_id):
    """
    :param post_id:
    :return: возвращает искомый пост в формате json
    """
    post = utils.get_post_by_pk(post_id)
    return jsonify(post)


if __name__ == '__main__':
    app.run()
