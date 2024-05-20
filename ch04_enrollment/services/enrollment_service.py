from models.enrollment import Enrollment

class EnrollmentService:
    def __init__(self):
        self.enrollment_db = Enrollment()
        
    def get(self):
        return [{'id':s[0],'student_number':s[1], 'student_name':s[2],
                 'course_name':s[3], 'professor':s[4], 'credit':s[5]} for s in self.enrollment_db.get()]
    
    def delete(self, id):
        self.enrollment_db.delete(id)
        
    def post(self, dto):
        self.check(dto)
        self.enrollment_db.post(dto)
        
    def check(self, dto):
        if self.enrollment_db.getOne(dto) != ():
            raise Exception('이미 존재하는 수강신청입니다.')