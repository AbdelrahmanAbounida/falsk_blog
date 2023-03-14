from app.extensions import mongo_db,login_manager, mongo_db
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self,id,email,password):
        self.id = id
        self.email = email
        self.password = password

    @staticmethod
    def is_authenticated():
        return True
    
    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False 
    
    def get_id(self):
        return self.id

