from flask import request, jsonify
from datetime import datetime
from .models import Post, db

# Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    # Get data from request
    data = request.get_json()

    # Create new post
    new_post = Post(
        post_id=data['post_id'],
        post_title=data['post_title'],
        post_body=data['post_body'],
        author_id=data['author_id'],
        timestamp=datetime.utcnow(),
        likes=0
    )

    # Add post to the database
    db.session.add(new_post)
    db.session.commit()

    # Return success message
    return jsonify({'message': 'Post created successfully.'})