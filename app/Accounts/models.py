from app.extensions import mongo_db,login_manager, mongo_db
class Account:
    def __init__(self,name,email,password) -> None:
        self.name = name
        self.email = email
        self.password = password


