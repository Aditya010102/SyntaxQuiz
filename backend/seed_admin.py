from app import app
from extensions import db
from models.user_model import User
from werkzeug.security import generate_password_hash

with app.app_context():

    admin = User.query.filter_by(
        email="admin@syntaxquiz.com"
    ).first()

    if admin:
        print("Admin already exists.")
    else:
        admin = User(
            full_name="Administrator",
            email="admin@syntaxquiz.com",
            password=generate_password_hash("Admin@123"),
            role="admin",
            provider="local"
        )

        db.session.add(admin)
        db.session.commit()

        print("Admin created successfully.")