from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

Base = declarative_base()

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)
    duration = db.Column(db.Float)
    workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
    workout = db.relationship('Workout', backref=db.backref('exercises', lazy=True))

def get_json(self):
    return {
        'id': self.id,
        'name': self.name,
        'sets': self.sets,
        'reps': self.reps,
        'weight': self.weight,
        'duration': self.duration,
        'workout_id': self.workout_id
    }