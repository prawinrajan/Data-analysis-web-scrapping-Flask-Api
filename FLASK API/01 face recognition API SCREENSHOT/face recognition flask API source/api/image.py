import json
import sqlite3
import base64
from flask import Flask, request, g
from .utils import json_response, JSON_MIME_TYPE
import ast
app = Flask(__name__)


@app.before_request
def before_request():
    g.db = sqlite3.connect('/home/prawin/Downloads/two.sqlite')

@app.route('/image', methods=['POST'])
def create_data():
    try:
        data = request.json
        
        id = data['HomeId']
        img = data['image']
        

        g.db.execute("insert into new(id,image) values (?,?)", (id, img,))
        g.db.commit()
        return json_response(status=201)
    except Exception as e:
        print(e)
        #print('process failed')
        return json_response(status=400)


