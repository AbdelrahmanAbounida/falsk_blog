from pymongo import MongoClient

uri = 'mongodb+srv://aboneda:aboneda@cluster0.psahi.mongodb.net/?retryWrites=true&w=majority'

client = MongoClient(uri)
db = client['blogdb']

# db.test_collection.insert({'some_key': 'some_value'})
# db.create_collection('blog_collection')

if 'blog_collection' in db.list_collection_names():
    print('The collection exists.')
else:
    print('The collection does not exist.')