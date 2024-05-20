import pymysql

class Enrollment:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists enrollment1(
                id int auto_increment primary key,
                student_id int not null,
                course_id int not null,
                foreign key (student_id) references student1 (id),
                foreign key (course_id) references course1 (id),
                unique index(student_id, course_id)
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
    def get(self):
        sql = '''
            select e.id, s.number, s.name, c.name, c.professor, c.credit
            from enrollment1 e
                join student1 s on e.student_id = s.id
                join course1 c on e.course_id = c.id
            order by e.id;
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def getOne(self, dto):
        sql = f"select * from enrollment1 where student_id like '{dto.student_id}' and course_id like '{dto.course_id}'"
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def delete(self, id):
        sql = 'delete from enrollment1 where id = ' + id
        self.cur.execute(sql)
        self.db.commit()
    
    def post(self, dto):
        sql = f"insert into enrollment1(student_id, course_id) values('{dto.student_id}','{dto.course_id}')"
        self.cur.execute(sql)
        self.db.commit()