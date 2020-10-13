import json
import sqlite3
from flask import Flask, request, g
from .utils import json_response, JSON_MIME_TYPE
import ast
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['DATABASE_NAME'])

@app.route('/book',methods=['DELETE'])
def book_delete():
    d = request.json
    print(d)
    mdata = request.data
    mydata = mdata.decode('utf8')
    s = json.loads(mydata)
    da = json.dumps(s)
    data = ast.literal_eval(da)
    id=data['id']
    cursor =g.db.execute("SELECT * FROM book WHERE id=?;",(id,))
    # Check if book exists
    if cursor.fetchone()[0] == 0:
        # Doesn't exist. Return 404.
        abort(404)

    # Delete it

    g.db.execute("DELETE FROM book WHERE id=?;",(id,))
    #delete_query = 'DELETE FROM book WHERE book.id = :id'
    g.db.commit()

    return json_response(status=204)


@app.errorhandler(404)
def not_found(e):
    return '', 404
