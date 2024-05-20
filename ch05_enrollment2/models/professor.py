import pymysql

class Professor:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists professor(
                id int auto_increment primary key,
                name varchar(50) not null,
                major varchar(50) not null,
                email varchar(50) not null
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
    def get(self):
        sql = 'select * from professor'
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def post(self, dto):
        sql = f"insert into professor(name, major, email) values('{dto.name}', '{dto.major}', '{dto.email}')"
        self.cur.execute(sql)
        self.db.commit()
        
    def getOne(self, dto):
        sql = f"select * from professor where name like '{dto.name}' and major like '{dto.major}'"
        self.cur.execute(sql)
        return self.cur.fetchone()