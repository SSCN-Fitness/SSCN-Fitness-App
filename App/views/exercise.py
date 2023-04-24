from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from models import Exercise, Base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'

# Initialize the SQLAlchemy database object
db = SQLAlchemy(app)
Base.metadata.create_all(db.engine)

@app.route('/exercises', methods=['POST'])
def create_exercise():
    # Get the request data from the JSON payload
    name = request.json['name']
    sets = request.json['sets']
    reps = request.json['reps']
    weight = request.json['weight']
    duration = request.json['duration']
    workout_id = request.json['workout_id']

    # Create a new Exercise object and add it to the database
    exercise = Exercise(name=name, sets=sets, reps=reps, weight=weight, duration=duration, workout_id=workout_id)
    db.session.add(exercise)
    db.session.commit()

    # Return the new exercise as a JSON response
    return jsonify({'exercise': {
        'id': exercise.id,
        'name': exercise.name,
        'sets': exercise.sets,
        'reps': exercise.reps,
        'weight': exercise.weight,
        'duration': exercise.duration,
        'workout_id': exercise.workout_id
    }})