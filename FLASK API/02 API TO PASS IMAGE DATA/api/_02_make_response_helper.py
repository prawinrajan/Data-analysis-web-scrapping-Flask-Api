import json
from flask import Flask, make_response

app = Flask(__name__)

sensor_data=[{
     "HomeId":1 ,
    "time":13,
    "temperature":38,
    "Humidity":13,
    "ultrasonic_motion_sensor":1,
        "IR":1
}]


@app.route('/sensor_data')
def sensor_detail():
    content = json.dumps(sensor_data)

    response = make_response(
        content, 200, {'Content-Type': 'application/json'})
    # Check utils.json_response ;)

    return response
