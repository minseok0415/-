import pymysql

class Reservation:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists reservation(
                id int auto_increment primary key,
                name varchar(50) not null,
                email varchar(50) not null,
                phone varchar(50),
                num_guests int,
                date_time datetime,
                restaurant_id int not null,
                foreign key (restaurant_id) references restaurant (id)
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
    def get(self):
        sql = 'select * from reservation'
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def add(self, dto):
        sql = f"insert into reservation(name, email, phone, num_guests, date_time, restaurant_id) values('{dto.name}', '{dto.email}', '{dto.phone}', '{dto.num_guests}', '{dto.date_time}', '{dto.restaurant_id}')"
        self.cur.execute(sql)
        self.db.commit()
    
    def delete(self, id):
        sql = f"delete from reservation where id = {id}"
        self.cur.execute(sql)
        self.db.commit()