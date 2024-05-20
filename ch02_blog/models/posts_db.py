import pymysql


class PostDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()

    def get(self):
        sql = 'select * from posts'
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def getOne(self, id):
        sql = 'select * from posts where id = ' + id
        self.cur.execute(sql)
        return self.cur.fetchone()

    def add(self, post):
        sql = f"insert into posts (title, content, author) values('{post['title']}', '{post['content']}', '{post['author']}')"
        self.cur.execute(sql)
        self.db.commit()
        
    def update(self, post):
        sql = f"update posts set title='{post['title']}', content='{post['content']}', author='{post['author']}' where id={post['id']}"
        self.cur.execute(sql)
        self.db.commit()
    
    def delete(self, id):
        sql = 'delete from posts where id = ' + id
        self.cur.execute(sql)
        self.db.commit()