from  Newton_Breakout import db
from uuid import uuid4


def get_uuid():
    """Generate a unique id using uuid4()"""
    return uuid4().hex


class User(db.Model):
    '''user table DB model'''
    __tablename__ = 'user'
    id = db.Column(db.String(60), primary_key=True, default=get_uuid(), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255))

    scores = db.relationship('Score', back_populates='user')

    tourscores = db.relationship('TourScore', back_populates='user')

    def __init__(self, email, name, password):
        """initalize class"""
        self.id = get_uuid()
        self.email = email
        self.name = name
        self.password = password

    def insert(self):
        """Insert the current object into the database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the current object from the database"""
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        """return class data as string"""
        return f"User-> id: {self.id}, email: {self.email}, name: {self.name}"
    
    def format(self):
        """returns user data a dict"""
        return ({
            "id": self.id,
            "email": self.email,
            "name": self.name
        })