from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "maincrafts_secret_key"


# ---------------- DATABASE INIT ----------------
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Users table (Login/Register)
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT
        )
    ''')

    # Students table (CRUD)
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            course TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()


# ---------------- HOME ----------------
@app.route('/')
def home():
    return redirect('/login')


# ---------------- REGISTER ----------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                      (username, password))
            conn.commit()
        except:
            return "Username already exists!"

        conn.close()
        return redirect('/login')

    return render_template('register.html')


# ---------------- LOGIN ----------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE username=? AND password=?",
                  (username, password))
        user = c.fetchone()
        conn.close()

        if user:
            session['user'] = username
            return redirect('/dashboard')
        else:
            return "Invalid Credentials!"

    return render_template('login.html')


# ---------------- DASHBOARD ----------------
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect('/login')


# ---------------- ADD STUDENT (CREATE) ----------------
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        conn = sqlite3.connect('database.db')
        c = conn.cursor()

        c.execute("INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
                  (name, email, course))

        conn.commit()
        conn.close()

        return redirect('/students')

    return render_template('add_student.html')


# ---------------- VIEW STUDENTS (READ) ----------------
@app.route('/students')
def students():
    if 'user' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT * FROM students")
    data = c.fetchall()

    conn.close()

    return render_template('students.html', students=data)


# ---------------- EDIT STUDENT (UPDATE) ----------------
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if 'user' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        course = request.form['course']

        c.execute("UPDATE students SET name=?, email=?, course=? WHERE id=?",
                  (name, email, course, id))

        conn.commit()
        conn.close()
        return redirect('/students')

    c.execute("SELECT * FROM students WHERE id=?", (id,))
    student = c.fetchone()

    conn.close()

    return render_template('edit_student.html', student=student)


# ---------------- DELETE STUDENT ----------------
@app.route('/delete/<int:id>')
def delete_student(id):
    if 'user' not in session:
        return redirect('/login')

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("DELETE FROM students WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect('/students')


# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(debug=True)