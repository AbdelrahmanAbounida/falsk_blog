from app.extensions import mongo_db

class Post:
    def __init__(self,title,content,date,img_file) -> None:
        self.title = title
        self.content = content
        self.date = date
        self.img_file = img_file
    
    def save(self):
        posts = mongo_db.blog_collection
        post_data = {'title': self.title, 'content': self.content, 'date':self.date, 'img_file': self.img_file}
        result = posts.insert_one(post_data)
        return result.inserted_id
