import json
import sqlite3
from flask import Flask, request, g
from .utils import json_response, JSON_MIME_TYPE
import ast
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect('Home.sqlite')

@app.route('/view_data')
def view_data():
    cursor = g.db.execute('SELECT HomeId, time, temperature,Humidity,ultrasonic_motion_sensor,IR FROM sensor_data;')
    sensor_data = [{
        'HomeId': row[0],
        'time': row[1],
        'temperature': row[2],
        'Humidity': row[3],
        'ultrasonic_motion_sensor': row[4],
        'IR':row[5]

    } for row in cursor.fetchall()]

    return json_response(json.dumps(sensor_data))

@app.route('/edit_data',methods=['PUT'])
def edit_data():
    try:
        d = request.json
        #print(d)
        mdata = request.data
        #mydata = mdata.decode('utf8')
        s = json.loads(mdata)

        da = json.dumps(s)
        remove_lef=da.replace('[','')
        remove_right=remove_lef.replace(']','')
        data = ast.literal_eval(remove_right)
        #print(data)
        id = data['HomeId']
        time= data['time']
        temp = data['temperature']
        h=data['Humidity']
        u=data['ultrasonic_motion_sensor']
        ir=data['IR']
        g.db.execute("""UPDATE sensor_data SET time= ?,temperature=?,Humidity=?,ultrasonic_motion_sensor=?,IR=? WHERE HomeId= ? """,(time, temp,   h, u, ir, id))
        g.db.commit()
        print("finish")
    except Exception as e:
        print(e)
        print('process failed')
    return json_response(status=201)
