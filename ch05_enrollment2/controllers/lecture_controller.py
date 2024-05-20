from flask import render_template, request, redirect, url_for, Blueprint, jsonify
from services.professor_service import ProfessorService
from services.course_service import CourseService
from services.lecture_service import LectureService
from utils.lectureDto import LectureFormDto

lecture_blueprint = Blueprint('lecture', __name__)
professor_service = ProfessorService()
course_service = CourseService()
lecture_service = LectureService()

@lecture_blueprint.route('/lecture_management')
def lecture_management():
    professors = professor_service.get()
    courses = course_service.get()
    lectures = lecture_service.get()
    return render_template('lecture_management.html', professors=professors, courses=courses, lectures=lectures)

@lecture_blueprint.route('/register_lecture', methods=['POST'])
def register_enrollment():
    lecture_service.post(LectureFormDto(request.form['professor_id'], request.form['course_id'], request.form['day'], request.form['start_time']))
    return redirect(url_for('lecture.lecture_management'))

@lecture_blueprint.route('/cancel_lecture', methods=['POST'])
def cancel_enrollment():
    lecture_service.delete(request.form['lecture_id'])
    return redirect(url_for('lecture.lecture_management'))

@lecture_blueprint.route('/api/student_lecture_list/<id>')
def student_lecture_list(id):
    lectures = lecture_service.getByStudent(id)
    response = jsonify(lectures)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@lecture_blueprint.route('/api/professor_lecture_list/<id>')
def professor_lecture_list(id):
    lectures = lecture_service.getByProfessor(id)
    response = jsonify(lectures)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response