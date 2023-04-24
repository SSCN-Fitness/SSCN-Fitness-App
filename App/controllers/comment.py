from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Comment, Base

app = Flask(__name__)

engine = create_engine('sqlite:///comments.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

@app.route('/comments', methods=['POST'])
def add_comment():
    # Get request data
    body = request.json['body']
    post_id = request.json['post_id']
    user_id = request.json['user_id']
    
    # Create comment object
    comment = Comment(body=body, post_id=post_id, user_id=user_id)
    
    # Add comment to database
    session = Session()
    session.add(comment)
    session.commit()
    
    return jsonify({'message': 'Comment added successfully.'}), 201