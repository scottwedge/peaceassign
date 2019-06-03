from db import db
from datetime import datetime

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    company_name = db.Column(db.String(80))
    city = db.Column(db.String(80))
    state = db.Column(db.String(80))
    zip_Code = db.Column(db.Integer)
    age = db.Column(db.Integer)
    website = db.Column(db.String(80) unique=True, nullable=False)				
    e_mail = db.Column(db.String(80) unique=True, nullable=False)				
    			

    def __init__(self, id, firstname, lastname, company_name, city, state, zip_code, age, website, email, ):
        self.id = id
    	self.firstname = firstname
    	self.lastname = lastname
    	self.company_name = company_name
        self.city = city
        self.state = state
	    self.zip_code = zip_code
    	self.age = age
    	self.email = email
        self.website = website

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()


    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()