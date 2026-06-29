# Student CRUD Management System

## Project Overview

The Student CRUD Management System is a Full Stack Web Application developed using **Python, Flask, SQLite, HTML, and CSS**. This application allows authenticated users to manage student records by performing **Create, Read, Update, and Delete (CRUD)** operations.

The project demonstrates the implementation of user authentication along with CRUD functionality, which is commonly used in real-world web applications for efficient data management.

---

## Features

- User Registration
- User Login
- User Logout
- Session Management
- Add Student
- View Student Records
- Update Student Details
- Delete Student Records
- SQLite Database Integration
- Dashboard Access for Authenticated Users
- Responsive User Interface

---

## Technologies Used

### Backend

- Python
- Flask

### Frontend

- HTML
- CSS

### Database

- SQLite

### Development Tools

- Visual Studio Code
- Web Browser

---

## Project Structure

```text

student-crud-management/
│
├── app.py
├── create_db.py
├── database.db
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── add_student.html
│   ├── students.html
│   └── edit_student.html
│
├── static/
│   └── style.css
│
└── README.md

```

---

## Application Flow

### User Registration

1. User enters a username and password.
2. Flask receives the registration data.
3. User details are stored in the SQLite database.
4. User is redirected to the Login page.

### User Login

1. User enters login credentials.
2. Flask validates the credentials against the database.
3. If valid, a session is created.
4. User is redirected to the Dashboard.

### Student Management

1. Authenticated users can access the student management dashboard.
2. Users can add new student records.
3. Users can view all student records.
4. Users can edit existing student details.
5. Users can delete student records from the database.

### Logout

1. User clicks the Logout button.
2. Session data is removed.
3. User is redirected to the Login page.

---

## Learning Outcomes

Through this project, I learned:

- Flask Routing
- User Authentication
- Session Handling
- SQLite Database Operations
- CRUD (Create, Read, Update, Delete) Operations
- Frontend and Backend Integration
- Full Stack Web Development Fundamentals

---

## Future Enhancements

- Password Hashing using Werkzeug
- Student Search Functionality
- Pagination for Student Records
- Student Profile with Image Upload
- Role-Based Authentication
- REST API Integration
- Responsive Dashboard Improvements