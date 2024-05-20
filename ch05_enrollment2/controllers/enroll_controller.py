from flask import render_template, request, redirect, url_for, Blueprint
from services.student_service import StudentService
from services.course_service import CourseService
from services.lecture_service import LectureService
from services.enrollment_service import EnrollmentService
from utils.enrollmentDto import EnrollmentFormDto

enroll_blueprint = Blueprint('enrollment', __name__)
student_service = StudentService()
course_service = CourseService()
lecture_service = LectureService()
enrollment_service = EnrollmentService()

@enroll_blueprint.route('/')
def index():
    return render_template('index.html')

@enroll_blueprint.route('/enrollment_management')
def enrollment_management():
    students = student_service.get()
    lectures = lecture_service.get()
    enrollments = enrollment_service.get()
    return render_template('enrollment_management.html', students=students, lectures=lectures, enrollments=enrollments)

@enroll_blueprint.route('/register_enrollment', methods=['POST'])
def register_enrollment():
    enrollment_service.post(EnrollmentFormDto(request.form['student_id'], request.form['lecture_id']))
    return redirect(url_for('enrollment.enrollment_management'))

@enroll_blueprint.route('/cancel_enrollment', methods=['POST'])
def cancel_enrollment():
    enrollment_service.delete(request.form['enrollment_id'])
    return redirect(url_for('enrollment.enrollment_management'))