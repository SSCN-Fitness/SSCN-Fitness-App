from flask import Blueprint, request, jsonify
from app.models.database import db
from app.models.workout import Workout, Exercise

workout_controller = Blueprint('workout_controller', __name__)

@workout_controller.route('/workouts', methods=['POST'])
def create_workout():
    # Get the request data from the JSON payload
    name = request.json['name']
    duration = request.json['duration']
    calories_burned = request.json['calories_burned']
    user_id = request.json['user_id']
    exercises = request.json.get('exercises', [])
    
    # Create a new Workout instance based on the user input
    workout = Workout(name=name, duration=duration, calories_burned=calories_burned, user_id=user_id)
    
    # Add exercises to the workout
    for exercise_data in exercises:
        exercise = Exercise(**exercise_data)
        workout.exercises.append(exercise)
    
    # Add the new workout record to the database
    db.session.add(workout)
    db.session.commit()
    
    # Return a JSON response with the new workout record data
    return jsonify({'workout': workout.to_dict()})