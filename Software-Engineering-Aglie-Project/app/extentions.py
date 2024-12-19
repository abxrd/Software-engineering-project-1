from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy() #extentions files added to fix global initiation issue
bcrypt = Bcrypt()