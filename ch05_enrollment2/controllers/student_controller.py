from flask import render_template, request, redirect, url_for, Blueprint, jsonify
from services.student_service import StudentService
from utils.studentDto import StudentFormDto

student_blueprint = Blueprint('student', __name__)
student_service = StudentService()

@student_blueprint.route('/student_management', methods=['GET', 'POST'])
def student_management():
    if request.method == 'GET':
        students = student_service.get()
        return render_template('student_management.html', students=students)
    if request.method == 'POST':
        student_service.post(StudentFormDto(request.form['number'], request.form['name'], request.form['gender']))
        return redirect(url_for('student.student_management'))
    
@student_blueprint.route('/api/student_list')
def lecture_list():
    students = student_service.get()
    response = jsonify(students)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response