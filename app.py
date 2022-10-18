from flask import Flask, render_template, request, jsonify, abort
from main.views import main_blueprint
from post.views import post_blueprint
from utils import search_for_posts, get_posts_by_user, get_posts_all, get_post_by_pk
import logging

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)


@app.route('/search')
def search_page():
    search = request.args['s']
    result = search_for_posts(search)
    len_result = len(result)
    if not result:
        return abort(404)
    else:
        return render_template('search.html', search=search, result=result, len_result=len_result)


@app.route('/users/<username>')
def user_name(username):
    list_users = get_posts_by_user(username)
    return render_template('user-feed.html', list_users=list_users)


@app.route('/api/posts')
def get_posts_json():
    logging.basicConfig(filename="./logs/api.log", format="%(asctime)s [%(levelname)s] %(message)s")
    posts = get_posts_all()
    return jsonify(posts)


@app.route('/api/posts/<int:pk>')
def get_post_json(pk):
    logging.basicConfig(filename="./logs/api.log", format="%(asctime)s [%(levelname)s] %(message)s")
    profile = get_post_by_pk(pk)
    return jsonify(profile)


app.run()

