class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.column(db.string(80))
    lastname = db.column(db.string(80))
    current_location = db.column(db.string(80))
    phone_number = db.Column(db.Integer)
    email = db.Column(db.string(80))				
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    created_at = db.Column(db.Integer)				
    updated_at = db.Column(db.Integer)				

    def __init__(self, firstname, lastname, current_location, phone_number, email, username, password, created_at, updated_at):
    	self.firstname = firstname
    	self.lastname = lastname
    	self.current_location = current_location
    	self.phone_number = phone_number
    	self.email = email
	    self.username = username
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at