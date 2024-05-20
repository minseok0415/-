from flask import render_template, request, redirect, url_for, Blueprint
from services.posts_service import PostService

posts_blueprint = Blueprint('posts', __name__)
posts_service = PostService()


@posts_blueprint.route('/')
def index():
    posts = posts_service.get_posts()
    return render_template('index.html', posts=posts)


@posts_blueprint.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if request.method == 'GET':
        return render_template('create.html')
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        posts_service.add_posts({'title': title, 'content': content, 'author': author})
        return redirect(url_for('posts.index'))


@posts_blueprint.route('/update_post/<postId>', methods=['GET', 'POST'])
def update(postId):
    if request.method == 'GET':
        post = posts_service.get_post(postId)
        return render_template('update.html', post=post)
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        posts_service.update_post({'id':postId, 'title': title, 'content': content, 'author': author})
        return redirect(url_for('posts.index'))
    
@posts_blueprint.route('/delete/<postId>')
def delete(postId):
    posts_service.delete_post(postId)
    return redirect(url_for('posts.index'))