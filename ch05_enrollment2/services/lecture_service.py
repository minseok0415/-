from models.lecture import Lecture

class LectureService:
    def __init__(self):
        self.lecture_db = Lecture()
        
    def get(self):
        results = [{'id':s[0],'course_name':s[1], 'professor_name':s[2], 'professor_major':s[3],
                 'credit':s[4], 'day':s[5], 'start_time':s[6], 'end_time':s[7]} for s in self.lecture_db.get()]
        for result in results:
            result['start_time'] = str(result['start_time'])
            result['end_time'] = str(result['end_time'])
        return results
    
    def getByStudent(self, id):
        results = [{'id':s[0],'course_name':s[1], 'professor_name':s[2], 'professor_major':s[3],
                 'credit':s[4], 'day':s[5], 'start_time':s[6], 'end_time':s[7]} for s in self.lecture_db.getByStudent(id)]
        for result in results:
            result['start_time'] = str(result['start_time'])
            result['end_time'] = str(result['end_time'])
        return results
    
    def getByProfessor(self, id):
        results = [{'id':s[0],'course_name':s[1], 'professor_name':s[2], 'professor_major':s[3],
                 'credit':s[4], 'day':s[5], 'start_time':s[6], 'end_time':s[7]} for s in self.lecture_db.getByProfessor(id)]
        for result in results:
            result['start_time'] = str(result['start_time'])
            result['end_time'] = str(result['end_time'])
        return results
    
    def delete(self, id):
        self.lecture_db.delete(id)
    
    def post(self, dto):
        if (self.duplicationCheck(dto)):
            self.lecture_db.post(dto)
        else:
            raise Exception('이미 등록된 강의입니다.')
            
    def duplicationCheck(self, dto):
        result = self.lecture_db.getOne(dto)
        print(result)
        return result == None