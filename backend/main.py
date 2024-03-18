from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date,Float
from dotenv import load_dotenv
import os

load_dotenv()

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)
app = Flask(__name__)
#print(os.getenv())
USERNAME,PASSWORD,HOST,DATABASE = os.getenv("PGUSER"),os.getenv("PGPASSWORD"),os.getenv("PGHOST"),os.getenv("PGDATABASE")
#app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?sslmode=require"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
class User(db.Model):
    __tablename__ = 'users'  # Optional: Customize table name

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    acc_type = Column(String(10),nullable=False)

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

@app.route("/")
def hello():
    return "Its working!"

@app.route("/api/signup",methods=["GET","POST"])
def signup():
    if request.method=="GET":
        return "Invalid Request"
    else:
        pass



if __name__ == "__main__":
    app.run(debug=os.getenv("DEBUG"))
