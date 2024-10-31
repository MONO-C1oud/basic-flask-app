from flask import *
from flask_sqlalchemy import * 
from datetime import datetime
import requests

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///firstapp.db"

with app.app_context():
    db = SQLAlchemy(app)

#db =  SQLAlchemy(app)

#now making a class to define the structure of our db
class FirstApp(db.Model):
    sno =  db.Column (db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(100), nullable=False)
    lname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(200), nullable=False)

    def _repr_(self): 
        return f"{self.sno} - {self.fname}"

@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    
    if request.method == 'POST':
        
        firstname = request.form.get('fname')
        lastname = request.form.get('lname')
        email = request.form.get('email')

        print(firstname)
        print(lastname)
        print(email)
        firstapp = FirstApp(fname=firstname, lname=lastname, email=email)
        db.session.add(firstapp)
        db.session.commit()

    allpeople = FirstApp.query.all()

    return render_template('index.html', allpeople=allpeople)

@app.route('/delete/<int:sno>', methods=['GET'])
def delete(sno):
    allpeople = FirstApp.query.filter_by(sno=sno).first()
    db.session.delete(allpeople)
    db.session.commit()

    return redirect("/")

@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    
    if request.method == 'POST':
        
        firstname = request.form.get('fname')
        lastname = request.form.get('lname')
        email = request.form.get('email')
        if firstname and lastname and email:
            allpeople = FirstApp.query.filter_by(sno=sno).first()
            allpeople.fname = firstname
            allpeople.lname = lastname
            allpeople.email = email
            db.session.add(allpeople)
            db.session.commit()
    
    
    allpeople = FirstApp.query.filter_by(sno=sno).first()

    return render_template('update.html',allpeople=allpeople)

@app.route('/home')
def home():
    return 'Welcome to the home page'

#Main function
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=80)