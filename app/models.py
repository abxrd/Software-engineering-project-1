from .extentions import db, bcrypt
from flask_login import UserMixin

# creating the User database and setting data types in model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(80), nullable=False, default='employee') # is the user 'manager' or 'employee'

    # using the bcrypt library to securely hash the users password on the server side
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {self.username}>'

# creating the Ticket database and setting data types in model
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    type_of_ticket = db.Column(db.String(80), nullable=False)
    priority_level = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='To DO', nullable=False)
    description = db.Column(db.Text, nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    tickets_assigned = db.relationship('User', backref='tickets', lazy=True)

    def __repr__(self):
        return '<Ticket {self.title}>'