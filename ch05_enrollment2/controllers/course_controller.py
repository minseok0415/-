from flask import render_template, request, redirect, url_for, Blueprint
from services.course_service import CourseService
from utils.courseDto import CourseFormDto

course_blueprint = Blueprint('course', __name__)
course_service = CourseService()

@course_blueprint.route('/course_management', methods=['GET', 'POST'])
def course_management():
    if request.method == 'GET':
        courses = course_service.get()
        return render_template('course_management.html', courses=courses)
    if request.method == 'POST':
        course_service.post(CourseFormDto(request.form['name'], request.form['credit']))
        return redirect(url_for('course.course_management'))