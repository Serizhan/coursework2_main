from flask import Blueprint, render_template
from utils import get_post_by_pk, get_comments_by_post_id

post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')


@post_blueprint.route('/post/<int:pk>')
def post_page(pk):
    profile = get_post_by_pk(pk)
    comments = get_comments_by_post_id(pk)
    len_comments = len(comments)
    return render_template('post.html', profile=profile, comments=comments, len_comments=len_comments)
