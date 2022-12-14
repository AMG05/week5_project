from flask import Flask, render_template

from controllers.member_controller import member_blueprint
from controllers.exercise_class_controller import exercise_class_blueprint
from controllers.booking_controller import bookings_blueprint


app = Flask(__name__)

app.register_blueprint(member_blueprint)
app.register_blueprint(exercise_class_blueprint)
app.register_blueprint(bookings_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)