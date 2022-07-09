import json
from json import JSONDecoder


def get_posts_all():
    """Возвращает посты"""
    try:
        with open("./data/data.json", 'r', encoding="utf-8") as file:
            profiles = json.loads(file.read())
        return profiles
    except JSONDecoder:
        return "Файл не удается преобразовать"


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя.
    Функция должна вызывать ошибку ValueError если такого пользователя
    нет и пустой список, если у пользователя нет постов."""
    list_users = []
    for user in get_posts_all():
        if user_name == user['poster_name']:
            list_users.append(user)
    return list_users


def get_comments_by_post_id(post_id):
    """Возвращает комментарии определенного поста. Функция должна вызывать ошибку
    ValueError если такого поста нет и пустой список, если у поста нет комментов. """
    try:
        with open("./data/comments.json", 'r', encoding="utf-8") as file:
            comments = json.loads(file.read())
            post_comment = []
            for comment in comments:
                if post_id == comment['post_id']:
                    post_comment.append(comment)
        return post_comment
    except JSONDecoder:
        return "Файл не удается преобразовать"


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    result = []
    for post in get_posts_all():
        if query.lower() in post['content'].lower():
            result.append(post)
    return result


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    for post in get_posts_all():
        if pk == post['pk']:
            return post

print(get_posts_by_user('df'))