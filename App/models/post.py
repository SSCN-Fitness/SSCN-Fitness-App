from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

Base = declarative_base()

class Post(Base):
    post_id = db.Column(db.String(50), primary_key= True, nullable =False)
    post_title = db.Column(db.String(50), nullable = False)
    post_body = db.Column(db.String(250), nullable = False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    author_id = db.Column(db.String(50), db.ForeignKey('user.username'), nullable=False)
    likes = Column(Integer, default=0)
    comments = relationship('Comment', backref='post', lazy='dynamic')





