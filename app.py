from flask import Flask, render_template,request, flash, redirect, url_for, jsonify , session
from flask import Response 
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

class name(Resource):
    def get(self):
        return{"data": "name"}

api.add_resource(name,"/name")

import db as db
@app.route('/')
def contact():
    
    return render_template('contact.html')

@app.route('/insert', methods = ['POST'])
def insert():
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        db.insert_details(name,email,message)
        details = db.get_details()
        print(details)
        for detail in details:
            var = detail
        return render_template('contact.html', var=var)
    
if __name__ == "__main__":
    
    app.run(host = 'localhost', port = '5000', debug=True)
        