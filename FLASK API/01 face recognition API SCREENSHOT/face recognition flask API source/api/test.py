import json
import sqlite3
from flask import Flask, request, g
from .utils import json_response, JSON_MIME_TYPE
import ast
app = Flask(__name__)


@app.before_request
def before_request():
    g.db = sqlite3.connect('Home.sqlite')


    #return json_response(json.dumps(sensor_data))

@app.route('/data/<int:HomeId>')
def sensor_detail(HomeId):

    id =HomeId
    cursor = g.db.execute("SELECT HomeId, time, temperature,Humidity,ultrasonic_motion_sensor,IR FROM sensor_data WHERE HomeId=?;", (id,))
    sensor_data = [{
        'HomeId': row[0],
        'time': row[1],
        'temperature': row[2],
        'Humidity': row[3],
        'ultrasonic_motion_sensor': row[4],
        'IR': row[5]

    } for row in cursor.fetchall()]

    return json_response(json.dumps(sensor_data))
