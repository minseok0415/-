from models.student import Student

class StudentService:
    def __init__(self):
        self.student_db = Student()
        
    def get(self):
        return [{'id':s[0], 'number':s[1], 'name':s[2], 'gender':s[3]} for s in self.student_db.get()]
    
    def post(self, dto):
        if (self.duplicationCheck(dto)):
            self.student_db.post(dto)
        else:
            raise Exception('이미 등록된 학생입니다.')
            
    def duplicationCheck(self, dto):
        result = self.student_db.getOne(dto)
        return result == None