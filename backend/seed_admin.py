from app import app
from extensions import db
from models.user_model import User
from werkzeug.security import generate_password_hash
from getpass import getpass

with app.app_context():

    email = input("Enter admin email: ")
    full_name = input("Enter admin name: ")
    password = getpass("Enter admin password: ")

    admin = User.query.filter_by(email=email).first()

    if admin:
        print("Admin already exists.")
    else:
        admin = User(
            full_name=full_name,
            email=email,
            password=generate_password_hash(password),
            role="admin",
            provider="local"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully.")