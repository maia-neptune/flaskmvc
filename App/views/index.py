from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import (
    create_user, initialize, create_and_confirm_ta,)
from App.controllers import *
from flask_jwt_extended import jwt_required

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})


# GET METHODS

# GET /teaching_assistant - retrieves a list of teaching assistants
# @index_views.route('/teaching_assistants', methods=['GET'])



# POST /lecturers – Create a lecturer (Admin only)
@index_views.route('/lecturers', methods=['POST'])
@jwt_required()  
def create_lecturer_view():
    data = request.get_json()
    prefix = data.get('prefix')
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    faculty = data.get('faculty')
    username = data.get('username')
    password = data.get('password')

    result = create_and_confirm_lecturer(prefix, firstName, lastName, faculty, username, password)

    if "Lecturer created" in result:
        return jsonify({"message": result}), 201
    else:
        return jsonify({"error": result}), 400




@index_views.route('/teaching_assistants', methods=['POST'])
@jwt_required()  
def create_teaching_assisstant_view():
    data = request.get_json()
    prefix = data.get('prefix')
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    faculty = data.get('faculty')
    username = data.get('username')
    password = data.get('password')

    result = create_and_confirm_ta(prefix, firstName, lastName, faculty, username, password)

    if "Lecturer created" in result:
        return jsonify({"message": result}), 201
    else:
        return jsonify({"error": result}), 400


@index_views.route('/tutors', methods=['POST'])
@jwt_required()  
def create_tutors_view():
    data = request.get_json()
    prefix = data.get('prefix')
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    faculty = data.get('faculty')
    username = data.get('username')
    password = data.get('password')

    result = create_and_confirm_tutor(prefix, firstName, lastName, faculty, username, password)

    if "Tutor created" in result:
        return jsonify({"message": result}), 201
    else:
        return jsonify({"error": result}), 400



@index_views.route('/courses/<int:course_id>/staff/lecturer', methods=['POST'])
def assign_lecturer_view():
    data = request.get_json()
    lecturer_id = data.get('id')
    
    if not lecturer_id:
        return jsonify({"message": "Missing lecturer ID."}), 400

    result = assign_lecturer(course_id, lecturer_id)
    return jsonify({"message": result}), 200


@index_views.route('/courses/<int:course_id>/staff/ta', methods=['POST'])
def assign_ta_view():
    data = request.get_json()
    ta_id = data.get('id')
    
    if not ta_id:
        return jsonify({"message": "Missing TA ID."}), 400

    result = assign_ta(course_id, ta_id)
    return jsonify({"message": result}), 200

@index_views.route('/courses/<int:course_id>/staff/tutor', methods=['POST'])
def assign_tutor_view():
    data = request.get_json()
    tutor_id = data.get('id')
    
    if not tutor_id:
        return jsonify({"message": "Missing tutor ID."}), 400

    result = assign_tutor(course_id, tutor_id)
    return jsonify({"message": result}), 200

