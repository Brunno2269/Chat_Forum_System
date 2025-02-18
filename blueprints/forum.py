from flask import Blueprint, render_template, request, redirect, url_for
from utils.data_manager import DataManager

forum_bp = Blueprint('forum', __name__)
data_manager = DataManager()

@forum_bp.route('/')
def index():
    topics = data_manager.get_topics()
    return render_template('index.html', topics=topics)

@forum_bp.route('/add_topic', methods=['POST'])
def add_topic():
    title = request.form.get('title')
    content = request.form.get('content')
    if title and content:
        data_manager.add_topic(title, content)
    return redirect(url_for('forum.index'))

@forum_bp.route('/add_comment/<int:topic_id>', methods=['POST'])
def add_comment(topic_id):
    comment = request.form.get('comment')
    if comment:
        data_manager.add_comment(topic_id, comment)
    return redirect(url_for('forum.index'))