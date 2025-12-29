# 🌿 Ambition Quiz – Online Quiz Platform (Django)

Ambition Quiz is a **full-stack Django web application** that allows users to attempt skill-based quizzes, view results instantly, track performance on a dashboard, and download certificates upon passing.

This project is designed to be **interview-ready**, beginner-friendly, and suitable for showcasing on **GitHub and LinkedIn**.

---

## 🚀 Features

- ✅ User Authentication (Login / Signup / Logout)
- 🧠 Skill-based quizzes (Python, Java, SQL, Kotlin, etc.)
- ⏱ Timed quizzes with auto-submit
- 📊 User Dashboard with quiz history & scores
- 🏆 Leaderboard based on total score
- 📄 Certificate generation (PDF) on passing (50%+)
- 🎨 Clean & modern UI (Bootstrap + custom CSS)
- 🔐 Secure (Django authentication & CSRF protection)

---

## 🛠 Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite (default Django DB)
- **Authentication:** Django Auth
- **PDF Generation:** ReportLab
- **Version Control:** Git & GitHub

---

## 📁 Project Structure
OnlineQuizProject/
│
├── online_quiz/
│ ├── manage.py
│ ├── db.sqlite3
│ ├── online_quiz/
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── wsgi.py
│ │
│ └── quiz/
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── admin.py
│ ├── migrations/
│ ├── templates/
│ │ └── quiz/
│ └── static/
│ └── quiz/
│ └── style.css
│
├── requirements.txt
└── Procfile

---

## ⚙️ How to Run This Project Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/maheklalu20-max/ambition-quiz.git
cd ambition-quiz

Step 2: Create and activate virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows

Step 3: Install dependencies
bash
Copy code
pip install -r requirements.txt

Step 4: Apply migrations
bash
Copy code
python manage.py migrate

Step 5: Create admin user
bash
Copy code
python manage.py createsuperuser

Step 6: Run the server
bash
Copy code
python manage.py runserver
Open in browser:


Visit: http://127.0.0.1:8000/

🔐 Admin Panel

URL: /admin

Add quizzes & questions from admin

View users and results

🎓 Certificate Logic

Passing score: 50% or above

Certificate includes:

Username

Quiz title

Score

Generated dynamically as PDF

🌐 Deployment

The project is deployment-ready and can be hosted on platforms like:

Railway

Render

PythonAnywhere

📌 Use Case

Practice platform for students

Interview preparation quizzes

Beginner-friendly demo website

Portfolio / LinkedIn showcase project

👩‍💻 Author

Mahek Lalu
Aspiring Software Developer | Django | Web Development

⭐ If you like this project, give it a star!

