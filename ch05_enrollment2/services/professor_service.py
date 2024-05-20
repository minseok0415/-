from models.professor import Professor

class ProfessorService:
    def __init__(self):
        self.professor_db = Professor()
        
    def get(self):
        return [{'id':s[0], 'name':s[1], 'major':s[2], 'email':s[3]} for s in self.professor_db.get()]
    
    def post(self, dto):
        if (self.duplicationCheck(dto)):
            self.professor_db.post(dto)
        else:
            raise Exception('이미 등록된 교수입니다.')
            
    def duplicationCheck(self, dto):
        result = self.professor_db.getOne(dto)
        return result == None