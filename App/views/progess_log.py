from flask import Blueprint, request, jsonify
from app.models.database import Session
from app.models.progress_log import ProgressLog

progress_log_controller = Blueprint('progress_log_controller', __name__)

@progress_log_controller.route('/progress_logs', methods=['POST'])
def create_progress_log():
    # Get the request data from the JSON payload
    date = request.json['date']
    workout_id = request.json['workout_id']
    exercise_id = request.json['exercise_id']
    sets_completed = request.json['sets_completed']
    reps_completed = request.json['reps_completed']
    weight_lifted = request.json['weight_lifted']
    duration_completed = request.json['duration_completed']
    calories_burned = request.json['calories_burned']

    # Create a new ProgressLog instance based on the user input
    progress_log = ProgressLog(date=date, workout_id=workout_id, exercise_id=exercise_id,
                               sets_completed=sets_completed, reps_completed=reps_completed,
                               weight_lifted=weight_lifted, duration_completed=duration_completed,
                               calories_burned=calories_burned)

    # Create a new session and add the new progress log record
    session = Session()
    session.add(progress_log)
    session.commit()

    # Close the session
    session.close()

    # Return a JSON response with the new progress log record data
    return jsonify({'progress_log': progress_log.to_dict()})