# Student Grades Management System API

A simple RESTful API built with **Flask**, **Flask-SQLAlchemy**, and **Docker**, designed to manage student grade records.

---

## 🧰 Features

- Add new student records
- View all students
- Retrieve student by ID
- Update student details
- Delete student records
- SQLite as the database
- Dockerized backend for portability

---

### 🐳 Run with Docker
1. Build Docker Image
```bash
docker build -t student-grade-flask .
```
2. Run Docker Container
```bash
docker run -p 5000:5000 student-grade-flask
```
App will be available at: http://localhost:5000

---

### Clone the Repository

```bash
git clone https://github.com/your-username/student-grades-api.git
cd student-grades-api
```

