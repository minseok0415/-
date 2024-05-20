from models.course import Course

class CourseService:
    def __init__(self):
        self.course_db = Course()
        
    def get(self):
        return [{'id':s[0], 'name':s[1], 'professor':s[2], 'credit':s[3]} for s in self.course_db.get()]
    
    def post(self, dto):
        self.check(dto)
        self.course_db.post(dto)
        
    def check(self, dto):
        if self.course_db.getOne(dto) != ():
            raise Exception('이미 존재하는 수업입니다.')