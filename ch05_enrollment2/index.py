from flask import Flask
from controllers.enroll_controller import enroll_blueprint
from controllers.course_controller import course_blueprint
from controllers.student_controller import student_blueprint
from controllers.professor_controller import professor_blueprint
from controllers.lecture_controller import lecture_blueprint

app = Flask(__name__)

app.register_blueprint(course_blueprint)
app.register_blueprint(student_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(lecture_blueprint)
app.register_blueprint(enroll_blueprint)

if __name__ == '__main__':
    app.run(debug=True)

# from models.course import Course
# Course()
# from models.professor import Professor
# Professor()
# from models.student import Student
# Student()

# from models.lecture import Lecture
# Lecture()

# from models.enrollment import Enrollment
# Enrollment()