import pymysql

class Enrollment:
    def __init__(self):
        self.db = pymysql.connect(host='localhost', user='root', password='1234', db='study')
        self.cur = self.db.cursor()
        
        sql = '''
            create table if not exists enrollment(
                id int auto_increment primary key,
                student_id int not null,
                course_id int not null,
                lecture_id int not null,
                foreign key (student_id) references student (id),
                foreign key (course_id) references course (id),
                foreign key (lecture_id) references lecture (id),
                unique index(student_id, course_id, lecture_id)
            )
        '''
        self.cur.execute(sql)
        self.db.commit()
        
    def get(self):
        sql = '''
            select e.id, s.number, s.name, c.name, p.name, c.credit
            from enrollment e
                join student s on e.student_id = s.id
                join course c on e.course_id = c.id
                join lecture l on e.lecture_id = l.id
                join professor p on l.professor_id = p.id
            order by e.id;
        '''
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def delete(self, id):
        sql = f'delete from enrollment where id = {id}'
        self.cur.execute(sql)
        self.db.commit()
    
    def post(self, dto):
        sql = f"select course_id from lecture where id = {dto.lecture_id}"
        self.cur.execute(sql)
        (course_id, ) = self.cur.fetchone()
        sql = f"insert into enrollment(student_id, course_id, lecture_id) values({dto.student_id}, {course_id}, {dto.lecture_id})"
        self.cur.execute(sql)
        self.db.commit()
    
    def getOne(self, dto):
        sql = f"select * from enrollment where student_id = {dto.student_id} and lecture_id = {dto.lecture_id}"
        self.cur.execute(sql)
        return self.cur.fetchone()