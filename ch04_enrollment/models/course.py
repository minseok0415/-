import pymysql

class Course:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists course1(
                id int auto_increment primary key,
                name varchar(50) not null,
                professor varchar(50) not null,
                credit int not null
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
    def get(self):
        sql = 'select * from course1'
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def getOne(self, dto):
        sql = f"select * from course1 where name like '{dto.name}' and professor like '{dto.professor}'"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def post(self, dto):
        sql = f"insert into course1(name, professor, credit) values('{dto.name}', '{dto.professor}', {dto.credit})"
        self.cur.execute(sql)
        self.db.commit()