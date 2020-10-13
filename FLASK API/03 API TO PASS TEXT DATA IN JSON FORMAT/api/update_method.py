import json
import sqlite3
from flask import Flask, request, g
from .utils import json_response, JSON_MIME_TYPE
import ast
app = Flask(__name__)

@app.before_request
def before_request():
    g.db = sqlite3.connect(app.config['DATABASE_NAME'])
@app.route('/edit_book')
def book_list():
    cursor = g.db.execute('SELECT id, author_id, title FROM book;')
    books = [{
        'id': row[0],
        'author_id': row[1],
        'title': row[2]
    } for row in cursor.fetchall()]

    return json_response(json.dumps(books))

@app.route('/edit_book',methods=['PUT'])
def book_create():
    try:
        d = request.json
        print(d)
        mdata = request.data
        mydata = mdata.decode('utf8')
        s = json.loads(mydata)
        da = json.dumps(s)
        data = ast.literal_eval(da)
        print(da)
        id = data['id']
        author = data['author_id']
        titl = data['title']
        g.db.execute("""UPDATE book SET author_id = ? ,title= ? WHERE id= ? """, (author, titl, id))
        g.db.commit()
        print("finish")
    except Exception as e:
        print(e)
    return json_response(status=201)
