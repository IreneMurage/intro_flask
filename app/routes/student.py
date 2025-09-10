from flask import Blueprint,jsonify,request

#create studen blueprint
student_bp = Blueprint("student", __name__)

#routes and controllers logic

@student_bp.route("/", methods=["GET"])
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>
<body>
    <h1>Welcome to my API</h1>
    <P>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Eos quidem et saepe nemo vitae sunt quis sequi accusantium ratione minima vel similique voluptas dolorum non earum repellendus a, libero dolore.</P>
</body>
</html>
    
    """

#ADD a student
@student_bp.route("/student/add", methods=["POST"])
def add_user():
    print ("Add user was hit")
    return "Adding a user"

@student_bp.route("/students",methods = ["GET"])
def list_users():
    print("List students")
    return "List All students: FROM"

