from flask import request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from extensions import db
from models.user_model import User
from services.google_auth_service import verify_google_token
from flask_jwt_extended import create_access_token


def register_user():

    data = request.get_json()

    full_name = data.get('full_name')
    email = data.get('email')
    password = data.get('password')

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "message": "Email already exists"
        }), 400

    hashed_password = generate_password_hash(password)

    new_user = User(
    full_name=full_name,
    email=email,
    password=hashed_password,
    provider="local"
)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201


def login_user():

    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({
            "message": "Invalid email"
        }), 401

    if user.provider == "google":
        return jsonify({
            "message": "Please login using Google."
        }), 400

    if not check_password_hash(user.password, password):
        return jsonify({
        "message": "Invalid password"
        }), 401

    access_token = create_access_token(identity=user.id)

    return jsonify({
        "message": "Login successful",
        "token": access_token,
        "user": {
            "id": user.id,
            "full_name": user.full_name,
            "email": user.email,
            "role": user.role
        }
    }), 200
def google_login():

    data = request.get_json()

    id_token = data.get("idToken")

    if not id_token:

        return jsonify({
            "message": "Google token is required"
        }), 400

    google_user = verify_google_token(id_token)

    if not google_user:

        return jsonify({
            "message": "Invalid Google Token"
        }), 401

    email = google_user["email"]

    name = google_user.get("name")

    google_id = google_user["sub"]

    user = User.query.filter_by(email=email).first()

    # Existing user
    if user:

        if user.provider == "local":

            return jsonify({
                "message": "This email is already registered using Email & Password. Please login normally."
            }), 400

        access_token = create_access_token(identity=user.id)

        return jsonify({

            "message": "Google Login Successful",

            "token": access_token,

            "user": {

                "id": user.id,

                "full_name": user.full_name,

                "email": user.email,

                "role": user.role

            }

        }), 200

    # New Google User

    new_user = User(

        full_name=name,

        email=email,

        password=None,

        provider="google",

        google_id=google_id

    )

    db.session.add(new_user)

    db.session.commit()

    access_token = create_access_token(identity=new_user.id)

    return jsonify({

        "message": "Google Login Successful",

        "token": access_token,

        "user": {

            "id": new_user.id,

            "full_name": new_user.full_name,

            "email": new_user.email,

            "role": new_user.role

        }

    }), 200