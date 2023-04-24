from flask import Blueprint, request, jsonify
from app.models.database import db
from app.models.workout import Workout

workout_controller = Blueprint('workout_controller', __name__)

@workout_controller.route('/workouts', methods=['POST'])
def create_workout():
    # Get the request data from the JSON payload
    name = request.json['name']
    duration = request.json['duration']
    calories_burned = request.json['calories_burned']
    user_id = request.json['user_id']
    
    # Create a new Workout instance based on the user input
    workout = Workout(name=name, duration=duration, calories_burned=calories_burned, user_id=user_id)
    
    # Add the new workout record to the database
    db.session.add(workout)
    db.session.commit()
    
    # Return a JSON response with the new workout record data
    return jsonify({'workout': workout.to_dict()})

@workout_controller.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    # Query the database for the workout record with the given ID
    workout = Workout.query.get_or_404(id)
    
    # Return a JSON response with the workout record data
    return jsonify({'workout': workout.to_dict()})