from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Float)
    calories_burned = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('workouts', lazy=True))
    exercises = db.relationship('Exercise', backref=db.backref('workout', lazy=True))

    def __repr__(self):
        return f"<Workout {self.name}>"


    def get_json(self):
        exercises_list = [e.get_json() for e in self.exercises]
        return {
            'id': self.id,
            'name': self.name,
            'duration': self.duration,
            'calories_burned': self.calories_burned,
            'user_id': self.user_id,
            'user': self.user.get_json(),
            'exercises': exercises_list
        }