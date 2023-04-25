from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

Base = declarative_base()

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True)
    body = Column(Text, nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref='comments')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User')


def get_json(self):
        return {
            'id': self.id,
            'body': self.body,
            'timestamp': self.timestamp.isoformat(),
            'post_id': self.post_id,
            'user_id': self.user_id
        }