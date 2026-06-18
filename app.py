from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "maincrafts_secret_key"


@app.route('/')
def home():
    return redirect('/login')


# Register
@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username, password)
        )

        conn.commit()
        conn.close()

        return redirect('/login')

    return render_template('register.html')


# Login
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:
            session['username'] = username
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"

    return render_template('login.html')


# Dashboard
@app.route('/dashboard')
def dashboard():

    if 'username' in session:
        return render_template(
            'dashboard.html',
            username=session['username']
        )

    return redirect('/login')


# Logout
@app.route('/logout')
def logout():

    session.pop('username', None)

    return redirect('/login')


if __name__ == '__main__':
    app.run(debug=True)