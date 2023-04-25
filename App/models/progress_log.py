from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

Base = declarative_base()

class ProgressLog(Base):
    __tablename__ = 'progress_logs'
    
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, nullable=False)
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    workout = relationship('Workout')
    exercise_id = Column(Integer, ForeignKey('exercises.id'))
    exercise = relationship('Exercise')
    sets_completed = Column(Integer)
    reps_completed = Column(Integer)
    weight_lifted = Column(Float)
    duration_completed = Column(Float)
    calories_burned = Column(Float)
    

    def get_json(self):
        return {
            'id': self.id,
            'date': str(self.date),
            'workout_id': self.workout_id,
            'workout_name': self.workout.name,
            'exercise_id': self.exercise_id,
            'exercise_name': self.exercise.name,
            'sets_completed': self.sets_completed,
            'reps_completed': self.reps_completed,
            'weight_lifted': self.weight_lifted,
            'duration_completed': self.duration_completed,
            'calories_burned': self.calories_burned
        }