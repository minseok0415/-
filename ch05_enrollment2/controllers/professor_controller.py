from flask import render_template, request, redirect, url_for, Blueprint, jsonify
from services.professor_service import ProfessorService
from utils.professorDto import ProfessorFormDto

professor_blueprint = Blueprint('professor', __name__)
professor_service = ProfessorService()

@professor_blueprint.route('/professor_management', methods=['GET', 'POST'])
def professor_management():
    if request.method == 'GET':
        professors = professor_service.get()
        return render_template('professor_management.html', professors=professors)
    if request.method == 'POST':
        professor_service.post(ProfessorFormDto(request.form['name'], request.form['major'], request.form['email']))
        return redirect(url_for('professor.professor_management'))
    
@professor_blueprint.route('/api/professor_list')
def lecture_list():
    professors = professor_service.get()
    response = jsonify(professors)
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response