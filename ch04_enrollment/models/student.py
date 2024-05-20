import pymysql

class Student:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists student1(
                id int auto_increment primary key,
                number int not null,
                name varchar(50) not null,
                gender varchar(10) not null
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
    def get(self):
        sql = 'select * from student1'
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def post(self, dto):
        sql = 'select * from student1 where number = ' + dto.number
        self.cur.execute(sql)
        result = self.cur.fetchall()
        if result == ():
            sql = f"insert into student1(number, name, gender) values({dto.number}, '{dto.name}', '{dto.gender}')"
            self.cur.execute(sql)
            self.db.commit()
        else:
            raise Exception('등록된 학번입니다')