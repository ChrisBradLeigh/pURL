from flask import Flask, request, redirect
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from markupsafe import escape
import json

db_connect = create_engine('sqlite:///purl.db')
app = Flask(__name__)
api = Api(app)

class pURL(Resource):
    def get(self, subpath):

        # Get URL of ShortURL from DB
        conn = db_connect.connect() # Create connection to DB
        query = conn.execute("select url from urls WHERE id = \"" + subpath + "\";") #Return URL from DB
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return redirect(result['data'][0]['url'], code=302)

api.add_resource(pURL, '/<subpath>')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5002')