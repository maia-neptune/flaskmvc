from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
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

