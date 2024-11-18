from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def home():
    return render_template('index.html', title="Home")

# About route
@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

# Contact route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Insert message into the database
        conn = get_db_connection()
        conn.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)",
                     (name, email, message))
        conn.commit()
        conn.close()

        return redirect(url_for('home'))

    return render_template('contact.html', title="Contact Us")

if __name__ == "__main__":
    app.run(debug=True)
