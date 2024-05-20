from models.course import Course

class CourseService:
    def __init__(self):
        self.course_db = Course()
        
    def get(self):
        return [{'id':s[0], 'name':s[1], 'credit':s[2]} for s in self.course_db.get()]
    
    def post(self, dto):
        if (self.duplicationCheck(dto)):
            self.course_db.post(dto)
        else:
            raise Exception('이미 등록된 수업입니다.')
            
    def duplicationCheck(self, dto):
        result = self.course_db.getOne(dto)
        return result == None