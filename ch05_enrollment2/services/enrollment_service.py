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
        if (self.duplicationCheck(dto)):
            self.enrollment_db.post(dto)
        else:
            raise Exception('이미 등록된 수강신청입니다.')
            
    def duplicationCheck(self, dto):
        result = self.enrollment_db.getOne(dto)
        return result == None