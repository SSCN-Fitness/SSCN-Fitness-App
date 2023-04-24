from flask import Flask, jsonify, request, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Post, Base

app = Flask(__name__)

engine = create_engine('sqlite:///posts.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

# Create a new blueprint
post_views = Blueprint('post_views', __name__)

@post_views.route('/posts', methods=['GET'])
def get_posts():
    session = Session()
    posts = session.query(Post).all()
    return jsonify({'posts': [post.to_dict() for post in posts]}), 200

@post_views.route('/posts', methods=['POST'])
def add_post():
    # Get request data
    post_id = request.json['post_id']
    post_title = request.json['post_title']
    post_body = request.json['post_body']
    author_id = request.json['author_id']
    
    # Create post object
    post = Post(post_id=post_id, post_title=post_title, post_body=post_body, author_id=author_id)
    
    # Add post to database
    session = Session()
    session.add(post)
    session.commit()
    
    return jsonify({'message': 'Post added successfully.'}), 201

@post_views.route('/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    session = Session()
    post = session.query(Post).filter_by(post_id=post_id).first()
    
    if post:
        return jsonify({'post': post.to_dict()}), 200
    else:
        return jsonify({'error': 'Post not found.'}), 404

@post_views.route('/posts/<post_id>', methods=['PUT'])
def update_post(post_id):
    # Get request data
    post_title = request.json.get('post_title')
    post_body = request.json.get('post_body')
    
    # Update post
    session = Session()
    post = session.query(Post).filter_by(post_id=post_id).first()
    
    if post:
        if post_title:
            post.post_title = post_title
        if post_body:
            post.post_body = post_body
        
        session.commit()
        return jsonify({'message': 'Post updated successfully.'}), 200
    else:
        return jsonify({'error': 'Post not found.'}), 404

@post_views.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    session = Session()
    post = session.query(Post).filter_by(post_id=post_id).first()
    
    if post:
        session.delete(post)
        session.commit()
        return jsonify({'message': 'Post deleted successfully.'}), 200
    else:
        return jsonify({'error': 'Post not found.'}), 404

# Register the blueprint with the app
app.register_blueprint(post_views)