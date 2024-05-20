from models.posts_db import PostDB


class PostService:
    def __init__(self):
        self.post_db = PostDB()

    def get_posts(self):
        return self.post_db.get()
    
    def get_post(self, id):
        return self.post_db.getOne(id)

    def add_posts(self, post):
        self.post_db.add(post)
        
    def update_post(self, post):
        self.post_db.update(post)
        
    def delete_post(self, id):
        self.post_db.delete(id)