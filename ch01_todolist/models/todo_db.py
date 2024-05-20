import pymysql

class TodoDB:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
    def add(self, task):
        sql = f"insert into todo(task) values('{task['name']}')"
        self.cur.execute(sql)
        self.db.commit()