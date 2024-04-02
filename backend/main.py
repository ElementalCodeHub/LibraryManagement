from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import cross_origin,CORS
from sqlalchemy.orm import DeclarativeBase,relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date,Float
from dotenv import load_dotenv
import os
from random import randrange
from uuid import uuid4,uuid3,NAMESPACE_URL


load_dotenv()

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:1234/*"}})
#print(os.getenv())
USERNAME,PASSWORD,HOST,DATABASE = os.getenv("PGUSER"),os.getenv("PGPASSWORD"),os.getenv("PGHOST"),os.getenv("PGDATABASE")
#app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?sslmode=require"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:sudo@localhost/library"
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///projects.db"
db.init_app(app)
class User(db.Model):
    __tablename__ = 'users'  # Optional: Customize table name

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255),nullable=False)
    salt = Column(String(255),nullable=False)
    acctype = Column(String(10),nullable=False)

class Book(db.Model):
    __tablename__ = 'books'  # Optional: Customize table name

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    author = Column(String(80), nullable=False)
    is_issued = Column(Boolean)
    issued_to = Column(Integer, ForeignKey('users.id'))
    issued_date = Column(Date)
    price = Column(Float)
    date_published = Column(Date)
    quantity = Column(Integer)

    user = relationship(User, backref='books')  # Optional relationship for convenience


with app.app_context():
    db.create_all()

def genSalt():
    x=""
    y=uuid4()
    z=[1,2,3,4,5,6,7,8,9,0]
    b=["a","b","c","d","e","f","g","h","i","j"]
    for i in range(10):
        a=randrange(0,10)
        x += (str(z[i]) + str(b[i]))
    return str(y) + x
    


@app.route("/")
def hello():
    return "Its working!"


@app.route("/api/user/<id>")
@cross_origin(origins="http://127.0.0.1:1234/*")
def getuser(id):
    x=db.session.execute(db.select(User).filter_by(id=id)).scalar()
    if(bool(x)):
        name,username,email,acctype=x.name,x.username,x.email,x.acctype
        return {"name":name,"username":username}
    else:
        return {"error":404,"msg":"User not found"}




@app.route("/api/signup",methods=["GET","POST"])
@cross_origin(origins="http://127.0.0.1:1234/*")
def signup():
    if request.method=="GET":
        return "Invalid Request"
    elif request.method=="POST":
        x=request.get_json(force=True)
        name,username,email,password,acctype=x["name"],x["username"],x["email"],x["password"],x["acctype"]
        salt = genSalt()
        hashedP = str(uuid3(NAMESPACE_URL,password+salt))
        user = User(
            name=name,
            username=username,
            email=email,
            password=hashedP,
            salt = salt,
            acctype=acctype
        )
        x=db.session.execute(db.select(User).filter_by(username=username)).scalar()
        if(not(bool(x))):
            db.session.add(user)
            db.session.commit()
            print("S")
            x=db.session.execute(db.select(User).filter_by(username=username)).scalar()
            return {"Success":200,"data":{"_id":x.id,"accType":x.acctype}},200
        else:
            return {"error":"Account already exists"},409
    else:
        pass


@app.route("/api/login",methods=["GET","POST"])
@cross_origin(origins="http://127.0.0.1:1234/*")
def login():
    if request.method=="GET":
        return "Invalid Request"
    elif request.method=="POST":
        x=request.get_json(force=True)
        username,password=x["username"],x["password"]
        y=db.session.execute(db.select(User).filter_by(username=username)).scalar()
        if not(y):
            return {"Error":404,"msg":"Account Not Found"},404
        elif y.password==str(uuid3(NAMESPACE_URL,password+y.salt)):
            return {"Success":200,"data":{"_id":y.id,"accType":y.acctype}},200
        elif y.password!=str(uuid3(NAMESPACE_URL,password+y.salt)):
            return {"Error":500,"msg":"Wrong password"},500
        


if __name__ == "__main__":
    if(os.getenv("DEBUG")=="" or os.getenv("DEBUG")==" " or os.getenv("DEBUG")=="False"):

        app.run(debug=False,port=8000)
    else:
        app.run(debug=True,host="localhost",port="8000")
