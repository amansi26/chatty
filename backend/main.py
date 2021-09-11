import sqlite3
from flask import Flask, request
from flask_restful import Api, Resource, reqparse
#import uuids
from hashids import Hashids
import user_create as uc

def get_db_connection():
    conn = sqlite3.connect('user_creation.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)
api = Api(app)

class User(Resource):
    def post(self):
        try:
            conn = get_db_connection()
            if request.method == 'POST':
                #user = request.form['user_number']
                #pwd = request.form['pwd']
                parser = reqparse.RequestParser()
                parser.add_argument('user', required=True)
                parser.add_argument('pwd', required=True)

                args = parser.parse_args()
                user = args['user']
                pwd = args['pwd']
                rc = uc.create_user_db(conn, user, pwd)
                if rc:
                    return {'message': 'Updated'}, 200
            return {'message': 'ISSUE IS THERE'}, 404
                
        except:
            return {'message': 'ISSUE'}, 404

    def delete(self):
        try:
            conn = get_db_connection()
            if request.method == 'DELETE':
                #user = request.form['user_number']
                parser = reqparse.RequestParser()
                parser.add_argument('user', required=True)

                args = parser.parse_args()
                user = args['user']
                rc = uc.remove_user_db(conn, user)
                if rc:
                    return {'message': 'Updated'}, 200
            return {'message': 'ISSUE IS THERE'}, 404
                
        except:
            return {'message': 'ISSUE'}, 404



api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run()
