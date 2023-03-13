# from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_login import LoginManager

##################
## Database
##################
# mongo = PyMongo()
mongo_client = MongoClient("mongodb+srv://aboneda:aboneda@cluster0.psahi.mongodb.net/?retryWrites=true&w=majority")
mongo_db = mongo_client['blogdb']

# create colection name
collection_name = 'blog_collection'
if not collection_name in mongo_db.list_collection_names():
    mongo_db.create_collection(collection_name)

##################
## Authentication
##################  
login_manager = LoginManager()
