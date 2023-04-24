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