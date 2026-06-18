# User Authentication System

## Project Overview

The User Authentication System is a Full Stack Web Application developed using **Python, Flask, SQLite, HTML, and CSS**. This application allows users to register, log in securely, access a dashboard, and log out of the system.

The project demonstrates the implementation of authentication mechanisms commonly used in real-world web applications.

---

## Features

- User Registration
- User Login
- User Logout
- Session Management
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
user_authentication_system/
│
├── app.py
├── create_db.py
├── database.db
│
├── templates/
│   ├── register.html
│   ├── login.html
│   └── dashboard.html
│
├── static/
│   └── style.css
│
└── README.md
```

---

## Authentication Flow

### User Registration

1. User enters username and password.
2. Flask receives registration data.
3. User details are stored in the SQLite database.
4. User is redirected to the Login page.

### User Login

1. User enters login credentials.
2. Flask validates the credentials against the database.
3. If valid, a session is created.
4. User is redirected to the Dashboard.

### Dashboard

1. Only authenticated users can access the dashboard.
2. The dashboard displays a welcome message.

### Logout

1. User clicks the Logout button.
2. Session data is removed.
3. User is redirected to the Login page.

## Learning Outcomes

Through this project, I learned:

- Flask Routing
- Authentication Systems
- Session Handling
- SQLite Database Operations
- Frontend and Backend Integration
- Full Stack Web Development Fundamentals

---

## Future Enhancements

- Password Hashing using Werkzeug
- Forgot Password Functionality
- Email Verification
- User Profile Management
- Role-Based Authentication
- REST API Integration