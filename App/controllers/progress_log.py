from flask import Flask, jsonify, request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from models import Base, ProgressLog, Workout, Exercise

app = Flask(__name__)

# Connect to the database
engine = create_engine('sqlite:///fitness.db')
Session = sessionmaker(bind=engine)
session = Session()

# Define the Flask route for the progress log function
@app.route('/progress', methods=['POST'])
def handle_progress_log():
    # Get the request data from the JSON payload
    date_str = request.json['date']
    date = datetime.strptime(date_str, '%Y-%m-%d').date()
    workout_id = request.json['workout_id']
    exercise_id = request.json['exercise_id']
    sets_completed = request.json['sets_completed']
    reps_completed = request.json['reps_completed']
    weight_lifted = request.json['weight_lifted']
    duration_completed = request.json['duration_completed']
    calories_burned = request.json['calories_burned']
    
    # Create a new progress log object with the provided parameters
    progress_log = ProgressLog(date=date, workout_id=workout_id, exercise_id=exercise_id,
                               sets_completed=sets_completed, reps_completed=reps_completed,
                               weight_lifted=weight_lifted, duration_completed=duration_completed,
                               calories_burned=calories_burned)
    
    # Add the progress log object to the session and commit the transaction
    session.add(progress_log)
    session.commit()
    
    # Return a success message as a JSON response
    return jsonify({'message': 'Progress log created successfully'})