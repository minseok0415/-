import pymysql

class Lecture:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists lecture(
                id int auto_increment primary key,
                professor_id int not null,
                course_id int not null,
                day varchar(10) not null,
                start_time time not null,
                foreign key (professor_id) references professor (id),
                foreign key (course_id) references course (id),
                unique index(professor_id, course_id)
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
    def get(self):
        sql = '''
            select l.id, c.name, p.name, p.major, c.credit, l.day, l.start_time, adddate(l.start_time, interval c.credit hour)
            from lecture l
                join professor p on l.professor_id = p.id
                join course c on l.course_id = c.id
            order by l.id;
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def getByStudent(self, id):
        sql = f'''
            select l.id, c.name, p.name, p.major, c.credit, l.day, l.start_time, adddate(l.start_time, interval c.credit hour)
            from enrollment e
                join lecture l on e.lecture_id = l.id
                join course c on e.course_id = c.id
                join student s on e.student_id = s.id
                join professor p on l.professor_id = p.id
            where s.number = {id}
            order by l.id;
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()
        
    def getByProfessor(self, id):
        sql = f'''
            select l.id, c.name, p.name, p.major, c.credit, l.day, l.start_time, adddate(l.start_time, interval c.credit hour)
            from lecture l
                join professor p on l.professor_id = p.id
                join course c on l.course_id = c.id
            where p.id = {id}
            order by l.id;
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def delete(self, id):
        sql = f'delete from lecture where id = {id}'
        self.cur.execute(sql)
        self.db.commit()
    
    def post(self, dto):
        sql = f"insert into lecture(professor_id, course_id, day, start_time) values({dto.professor_id}, {dto.course_id}, '{dto.day}', '{dto.start_time}')"
        self.cur.execute(sql)
        self.db.commit()
    
    def getOne(self, dto):
        sql = f"select * from lecture where professor_id = {dto.professor_id} and course_id = {dto.course_id}"
        self.cur.execute(sql)
        return self.cur.fetchone()