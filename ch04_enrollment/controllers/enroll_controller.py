from flask import render_template, request, redirect, url_for, Blueprint
from services.student_service import StudentService
from services.course_service import CourseService
from services.enrollment_service import EnrollmentService
from utils.dto import StudentFormDto, CourseFormDto, EnrollmentFormDto

enroll_blueprint = Blueprint('enrollment', __name__)
student_service = StudentService()
course_service = CourseService()
enrollment_service = EnrollmentService()

@enroll_blueprint.route('/')
def index():
    return render_template('index.html')

@enroll_blueprint.route('/student_management', methods=['GET', 'POST'])
def student_management():
    if request.method == 'GET':
        students = student_service.get()
        return render_template('student_management.html', students=students)
    if request.method == 'POST':
        student_service.post(StudentFormDto(request.form['number'], request.form['name'], request.form['gender']))
        return redirect(url_for('enrollment.student_management'))

@enroll_blueprint.route('/course_management', methods=['GET', 'POST'])
def course_management():
    if request.method == 'GET':
        courses = course_service.get()
        return render_template('course_management.html', courses=courses)
    if request.method == 'POST':
        course_service.post(CourseFormDto(request.form['name'], request.form['professor'], request.form['credit']))
        return redirect(url_for('enrollment.course_management'))

@enroll_blueprint.route('/enrollment_management')
def enrollment_management():
    students = student_service.get()
    courses = course_service.get()
    enrollments = enrollment_service.get()
    return render_template('enrollment_management.html', students=students, courses=courses, enrollments=enrollments)

@enroll_blueprint.route('/register_enrollment', methods=['POST'])
def register_enrollment():
    enrollment_service.post(EnrollmentFormDto(request.form['student_id'], request.form['course_id']))
    return redirect(url_for('enrollment.enrollment_management'))

@enroll_blueprint.route('/cancel_enrollment', methods=['POST'])
def cancel_enrollment():
    enrollment_service.delete(request.form['enrollment_id'])
    return redirect(url_for('enrollment.enrollment_management'))