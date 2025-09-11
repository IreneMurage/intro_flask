from flask import Blueprint,jsonify,request

#create studen blueprint
student_bp = Blueprint("student", __name__, url_prefix = "/student")

#routes and controllers logic

@student_bp.route("/", methods=["GET"])
def home():
    print("Single student")
    return "SIngle student"

#ADD a student
@student_bp.route("/add", methods=["POST"])
def add_user():
    print ("Add user was hit")
    return "Adding a user"

@student_bp.route("/edit", methods=["PUT"])
def edit_user():
    print ("Add user was successful")
    return "Editing a user"


@student_bp.route("/list",methods = ["GET"])
def list_users():
    print("List students")
    return "List All students: FROM"

