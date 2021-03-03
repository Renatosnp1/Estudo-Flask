from app import db

class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(50), unique=True)
    passWord = db.Column(db.String(8))
    name = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)

    def __init__(self, userName, passWord, name, email):
        self.userName = userName
        self.passWord = passWord
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.userName