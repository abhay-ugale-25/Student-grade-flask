from flask_sqlalchemy import  SQLAlchemy
db = SQLAlchemy()
class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    subject = db.Column(db.String(50))
    grade = db.Column(db.Float)

