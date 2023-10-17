from  Newton_Breakout import db
from uuid import uuid4

def get_uuid():
    """Generate a unique id using uuid4()"""
    return uuid4().hex



class TourScore(db.Model):
    '''Tournament table model class'''
    __tablename__ = 'tourscore'
    id = db.Column(db.String(60), primary_key=True, default=get_uuid(), unique=True, nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey(
        "user.id"), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='tourscores')

    def __init__(self, user_id, score):
        '''initalize class'''
        self.id = get_uuid()
        self.user_id = user_id
        self.score = score

    def insert(self):
        """Insert the current object into the database"""
        db.session.add(self)
        db.session.commit()

    def delete(self):
        """Delete the current object from the database"""
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        '''return class data as string'''
        return f"User-> id: {self.id}, user_id: {self.user_id}, score: {self.score}"
    
    def format(self):
        '''return score data as dict'''
        return ({
            "id": self.id,
            "user_id": self.user_id,
            "score": self.score
        })