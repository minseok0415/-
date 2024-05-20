class LectureFormDto:
    def __init__(self, professor_id, course_id, day, start_time):
        self._professor_id = professor_id
        self._course_id = course_id
        self._day = day
        self._start_time = start_time
    
    @property
    def professor_id(self):
        return self._professor_id
    
    @property
    def course_id(self):
        return self._course_id
    
    @property
    def day(self):
        return self._day
    
    @property
    def start_time(self):
        return self._start_time