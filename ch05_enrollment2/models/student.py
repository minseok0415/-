import pymysql

class Student:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists student(
                id int auto_increment primary key,
                number int not null,
                name varchar(50) not null,
                gender varchar(10) not null
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
    def get(self):
        sql = 'select * from student'
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def post(self, dto):
        sql = f"insert into student(number, name, gender) values('{dto.number}', '{dto.name}', '{dto.gender}')"
        self.cur.execute(sql)
        self.db.commit()
        
    def getOne(self, dto):
        sql = f"select * from student where number = {dto.number}"
        self.cur.execute(sql)
        return self.cur.fetchone()