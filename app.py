from flask import Flask, render_template
from flask_socketio import SocketIO, send
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def intakeMessage(msg):
    print("Message: " + msg)

    # intake the message and pass it into GPT-3 use exec() and a try except block

    # then send the output or graph back to the user instead of the message here
    send(msg, broadcast=True)  # If broadcast is false it will only send to one user (want to do that in the future)


@app.route('/')
def home():

    return render_template('test_frontend.html')


if __name__ == '__main__':
    socketio.run(app)