from app.extensions import mongo_db

class Post:
    def __init__(self,title,content,date,background,use,category) -> None:
        self.title = title
        self.content = content
        self.date = date
        self.background = background
        self.user = user
        self.category = category
        
    def save(self):
        posts = mongo_db.blog_collection
        post_data = {'title': self.title, 
                     'content': self.content, 
                     'date':self.date, 
                     'background': self.background,
                     'user':self.user,
                     'category':self.category}

        result = posts.insert_one(post_data)
        return result.inserted_id
