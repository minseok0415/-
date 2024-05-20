import pymysql

class Restaurant:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists restaurant(
                id int auto_increment primary key,
                name varchar(50) not null,
                address varchar(50) not null,
                phone varchar(50) not null
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
        datas = [['낙동강오리알', '부산 강서구 상덕로 35-1', '0507-1339-8873'],
                 ['컴포즈커피', '부산 강서구 호계로 8 1층', '0507-1416-5421']]
        
        for data in datas:
            sql = f'''
                insert into restaurant(name, address, phone)
                select '{data[0]}', '{data[1]}', '{data[2]}' from dual
                where not exists
                (select name, address, phone from restaurant
                where name = '{data[0]}' and address = '{data[1]}' and phone = '{data[2]}')
            '''
            self.cur.execute(sql)
            
        self.db.commit()
        
    def get(self):
        sql = 'select * from restaurant'
        self.cur.execute(sql)
        return self.cur.fetchall()