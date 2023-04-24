from flask import Flask, render_template, request, redirect, url_for
from exercise import db, Exercise

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'

# Initialize the SQLAlchemy database object
db.init_app(app)

@app.route('/exercises/create', methods=['GET', 'POST'])
def create_exercise():
    if request.method == 'POST':
        name = request.form['name']
        sets = request.form['sets']
        reps = request.form['reps']
        weight = request.form['weight']
        duration = request.form['duration']
        workout_id = request.form['workout_id']

        exercise = Exercise(name=name, sets=sets, reps=reps, weight=weight, duration=duration, workout_id=workout_id)
        db.session.add(exercise)
        db.session.commit()

        return redirect(url_for('get_exercise', exercise_id=exercise.id))

    return render_template('create_exercise.html')

@app.route('/exercises/<int:exercise_id>', methods=['GET'])
def get_exercise(exercise_id):
    exercise = Exercise.query.get_or_404(exercise_id)
    return render_template('exercise.html', exercise=exercise)