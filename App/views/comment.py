from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Comment, Base

app = Flask(__name__)

# Create engine and sessionmaker for database
engine = create_engine('sqlite:///comments.db')
Session = sessionmaker(bind=engine)

# Create tables if they do not exist
Base.metadata.create_all(engine)

# Create a blueprint for comment views
comment_views = Blueprint('comment_views', __name__)

# Define view for getting all comments
@comment_views.route('/comments', methods=['GET'])
def get_comments():
    # Open session to database
    session = Session()
    # Query all comments from database
    comments = session.query(Comment).all()
    comments_list = []
    for comment in comments:
        # Create dictionary for each comment
        comments_list.append({
            'id': comment.id,
            'body': comment.body,
            'timestamp': comment.timestamp,
            'post_id': comment.post_id,
            'user_id': comment.user_id
        })
    # Close session
    session.close()
    return jsonify(comments_list), 200