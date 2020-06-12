from flask import Flask, request, redirect, url_for
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from markupsafe import escape
import os
import string
import random
import json

db_connect = create_engine('sqlite:///purl.db')
app = Flask(__name__)
api = Api(app)

#Some Variable Declerations from ENV Vars
default_url = os.environ.get('PURL_DEFAULT_URL')
host_url = os.environ.get('PURL_HOST_URL')

class pURL(Resource):
    def get(self, subpath):
        #reconstruct path to url with args
        for i in request.args.keys():
            if "?" in subpath:
                subpath += "&"
            else:
                subpath += "?"
            subpath += i + "=" + request.args.get(i)
        print(subpath)
        #Check the subpath, if match URL format, generate a url, else redirect
        if subpath[:4] == "http":
            #check if url already exists in DB
            conn = db_connect.connect()
            query = conn.execute("select * from urls WHERE url = \"" + subpath + "\";")
            result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
            if len(result['data']) > 0:
                return(host_url + result['data'][0]['id'])
            #generate random string:
            rString = ""
            for x in range(5):
                rString += random.choice(string.ascii_letters)
            #add to DB
            conn = db_connect.connect() # Create connection to DB
            query = conn.execute("INSERT INTO urls(id, url) VALUES (\"" + rString + "\", \"" + subpath + "\");")
            return(host_url + rString)
        else:
            # Get URL of ShortURL from DB
            try:
                conn = db_connect.connect() # Create connection to DB
                query = conn.execute("select url from urls WHERE id = \"" + subpath + "\";") #Return URL from DB
                result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]} #get result in JSON format
                print(result['data'][0]['url'])
                return redirect(result['data'][0]['url'], code=302) # send client 302 based on url in DB
            except:
                return redirect(default_url, code=302)

api.add_resource(pURL, '/<path:subpath>')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port='5002')
