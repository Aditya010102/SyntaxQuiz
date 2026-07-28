<div align="center">

# 🚀 SyntaxQuiz

### A Modern Full Stack Quiz Platform Built with Angular, Flask & MySQL

A production-ready quiz platform where users can register, log in securely, sign in with Google, attempt programming quizzes, and track their learning progress.

<p>

![Angular](https://img.shields.io/badge/Angular-21-DD0031?style=for-the-badge&logo=angular&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-REST%20API-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Railway-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-success?style=for-the-badge)
![Google OAuth](https://img.shields.io/badge/Login-Google%20OAuth-4285F4?style=for-the-badge&logo=google)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Render](https://img.shields.io/badge/Backend-Render-5A29E4?style=for-the-badge)
![Vercel](https://img.shields.io/badge/Frontend-Vercel-000000?style=for-the-badge&logo=vercel)

</p>

</div>

---

# 🌐 Live Demo

## Frontend

👉 https://syntax-quiz-gamma.vercel.app/

## Backend API

👉 https://syntaxquiz-1.onrender.com

---

# 📖 About SyntaxQuiz

SyntaxQuiz is a modern full-stack web application designed for programming enthusiasts to practice coding concepts through interactive quizzes.

Users can securely register, log in using email/password or Google OAuth, choose subjects, attempt quizzes, and improve their programming knowledge.

The application follows a scalable REST API architecture using Angular as the frontend and Flask as the backend.

---

# ✨ Features

- 🔐 JWT Authentication
- 🔑 Google OAuth Login
- 👤 User Registration & Login
- 📚 Subject-wise Quizzes
- ❓ Dynamic Quiz Questions
- 📊 Score Calculation
- 📱 Responsive UI
- ⚡ Angular Standalone Components
- 🔄 RESTful API
- 🛡 Secure Password Hashing
- 🐳 Dockerized Backend
- ☁ Cloud Deployment
- 💾 MySQL Database

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Frontend | Angular 21 |
| Language | TypeScript |
| Styling | CSS3 |
| Backend | Flask |
| ORM | SQLAlchemy |
| Authentication | JWT + Google OAuth |
| Database | MySQL (Railway) |
| Deployment | Vercel + Render |
| Containerization | Docker |
| Version Control | Git & GitHub |

---

# 🏗 System Architecture

```text
                   +----------------------+
                   |    Angular 21 UI     |
                   +----------+-----------+
                              |
                              |
                         REST API Calls
                              |
                              ▼
                   +----------------------+
                   |     Flask Backend    |
                   | JWT Authentication   |
                   +----------+-----------+
                              |
                        SQLAlchemy ORM
                              |
                              ▼
                   +----------------------+
                   |    Railway MySQL     |
                   +----------------------+
```

---

# 📸 Screenshots

 -- In SyntaxQuiz Screenshot folder

# 📂 Folder Structure

```text
SyntaxQuiz
│
├── backend
│   ├── models
│   ├── routes
│   ├── config.py
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── ...
│
├── frontend
│   ├── src
│   ├── angular.json
│   ├── package.json
│   └── ...
│
├── SyntaxQuiz Screenshots
│   ├── Admin Dashboard.jpg
│   ├── login.jpg
│   ├── register.jpg
│   ├── dashboard.jpg
│   ├── quiz.jpg
│   └── leaderboard.jpg
│
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/Aditya010102/SyntaxQuiz.git

cd SyntaxQuiz
```

---

# 🔧 Backend Setup

```bash
cd backend

python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the server

```bash
python app.py
```

Backend runs on

```
http://127.0.0.1:5000
```

---

# 💻 Frontend Setup

```bash
cd frontend

npm install

ng serve
```

Frontend runs on

```
http://localhost:4200
```

---

# ⚙ Environment Variables

Create a `.env` file inside the backend folder.

```env
SECRET_KEY=your_secret_key

JWT_SECRET_KEY=your_jwt_secret

DATABASE_URL=your_mysql_database_url

GOOGLE_CLIENT_ID=your_google_client_id
```

---

## Create Admin

Run:

python seed_admin.py

The script will ask you for:

- Admin Name
- Admin Email
- Admin Password

# 📡 REST API

## Authentication

| Method | Endpoint | Description |
|----------|----------|-------------|
| POST | /api/auth/register | Register User |
| POST | /api/auth/login | User Login |
| POST | /api/auth/google-login | Google Login |

---

## Subjects

| Method | Endpoint |
|----------|----------|
| GET | /api/subjects |

---

## Questions

| Method | Endpoint |
|----------|----------|
| GET | /api/questions/<subject_id> |

---

# 🔐 Authentication Flow

```text
User Login
      │
      ▼
Flask Authentication
      │
      ▼
Generate JWT Token
      │
      ▼
Angular Stores Token
      │
      ▼
Protected API Requests
```

---

# ☁ Deployment

## Frontend

- Vercel

## Backend

- Render

## Database

- Railway MySQL

---

# 🎯 Future Improvements


- 📊 Quiz Analytics
- 🏆 Global Leaderboard
- ⏱ Quiz Timer
- 📧 Email Verification
- 🔁 Forgot Password
- 🌙 Dark Mode
- 📈 Progress Tracking
- 🎓 Quiz Certificates
- 🤖 AI Question Generator

---

# 👨‍💻 Developer

**Aditya Tiwari**

### GitHub

https://github.com/Aditya010102

### LinkedIn

https://linkedin.com/in/<Aditya Tiwari

LinkedIn: https://linkedin.com/in/adityatiwari112

GitHub: https://github.com/Aditya010102

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve SyntaxQuiz:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

<div align="center">

## ⭐ If you like this project, don't forget to star the repository!

Made with ❤️ by **Aditya Tiwari**

</div>
