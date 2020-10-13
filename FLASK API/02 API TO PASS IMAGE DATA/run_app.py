import os

#from api._01_manual_response_class import app
#from api._02_make_response_helper import app
#from api.post_method import app
#from api.delete import app
from api.image import app
#from api.test import app
#from api.update import app
# from api._05_flask_restful_simple import app


if __name__ == '__main__':
    app.debug = True
    app.config['DATABASE_NAME'] ='Home.sqlite'
    host = os.environ.get('IP', '0.0.0.0')
    port = int(os.environ.get('PORT', 8080))
    app.run(host=host, port=port)
