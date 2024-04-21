from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Set a secret key for session management

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to verify passwords
def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('easecampus.db')
    conn.row_factory = sqlite3.Row
    return conn

# Route for the login page
@app.route('/')
def login():
    return render_template('login.html')

# Route for handling login form submission
@app.route('/login', methods=['POST'])
def login_submit():
    email = request.form['email']
    password = request.form['password']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Query the database for the user with the provided email
    cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
    user = cursor.fetchone()

    if user:
        # If the user exists, verify the password
        if verify_password(user['password'], password):
            # If the password is correct, store the email in the session
            session['email'] = email
            session['enrollment_no'] = user['enrollment_no']
            conn.close()
            # Redirect to the home page
            return redirect(url_for('home'))
        else:
            # If the password is incorrect, show an error message
            return 'Invalid email or password. Please try again.'
    else:
        # If the user does not exist, show an error message
        return 'User does not exist. Please try again.'

# Route for the home page
@app.route('/home')
def home():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        # If email is stored in the session, render the home page with the email
        return render_template('home.html', user=user)
    else:
        # If email is not stored in the session, redirect to the login page
        return redirect(url_for('login'))

# Route for the profile page
@app.route('/profile')
def profile():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('profile.html', user=user)
    return 'User not found.'

@app.route('/course_reg')
def course_reg():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('course_reg.html', user=user)
    return 'User not found.'

@app.route('/feedback')
def feedback():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('feedback.html', user=user)
    return 'User not found.'

@app.route('/event')
def event():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('event.html', user=user)
    return 'User not found.'

@app.route('/exam')
def exam():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('exam.html', user=user)
    return 'User not found.'

@app.route('/calendar')
def calendar():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('calendar.html', user=user)
    return 'User not found.'

@app.route('/ticket_gen')
def ticket_gen():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('ticket_gen.html', user=user)
    return 'User not found.'

@app.route('/club')
def club():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('club.html', user=user)
    return 'User not found.'

# Route for the club details page
@app.route('/club_details')
def club_details():
    # Get the club name from the query parameter
    club_name = request.args.get('club')
    if club_name:
        # Query the database for club details based on the club name
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT club, club_logo FROM club_members WHERE club = ?", (club_name,))
        club_info = cursor.fetchone()
        cursor.execute("SELECT role, picture, name, email FROM club_members WHERE club = ?", (club_name,))
        club_members = cursor.fetchall()
        conn.close()

        # Query the database for the student currently in session
        session_email = session.get('email')
        if session_email:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE email = ?', (session_email,))
            session_student = cursor.fetchone()
            conn.close()
            return render_template('club_details.html', club_info=club_info, club_members=club_members, user=session_student)
        else:
            return 'User not found.'
    else:
        # If club name is not provided, return an error message or redirect to an error page
        return 'Club name not provided.'
    
@app.route('/lost_found')
def lost_found():
    email = session.get('email')
    if email:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students WHERE email = ?', (email,))
        user = cursor.fetchone()
        conn.close()
        if user:
            return render_template('lost&found.html', user=user)
    return 'User not found.'

# Function to save uploaded photo and return its path
def save_photo(photo):
    if photo:
        # Get the last used photo number
        last_photo_number = get_last_photo_number()
        next_photo_number = last_photo_number + 1

        # Create a file name with the next photo number
        filename = f"{next_photo_number}.jpg"
        photo_path = os.path.join('static', 'uploads', filename)
        photo.save(photo_path)
        return photo_path
    return None

# Function to get the last used photo number
def get_last_photo_number():
    uploads_dir = os.path.join(os.getcwd(), 'uploads')
    last_photo_number = 0
    if os.path.exists(uploads_dir):
        for filename in os.listdir(uploads_dir):
            if filename.endswith('.jpg'):
                photo_number = int(filename.split('.')[0])
                if photo_number > last_photo_number:
                    last_photo_number = photo_number
    return last_photo_number

@app.route('/submit_lost_item', methods=['POST'])
def submit_lost_item():
    if request.method == 'POST':
        # Extract form data
        item_name = request.form['itemName']
        keywords = request.form['Keywords']
        date_lost = request.form['dateLost']
        place_lost = request.form['placeLost']
        reference_photo = request.files['referencePhoto']
        enrollment_no = session.get('enrollment_no')

        # Save reference photo to a folder and get its path
        photo_path = save_photo(reference_photo)

        # Insert data into the lost_items table
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO lost_items (item_name, keywords, date_lost, place_lost, reference_photo, enrollment_no)
                          VALUES (?, ?, ?, ?, ?, ?)''', (item_name, keywords, date_lost, place_lost, photo_path, enrollment_no))
        conn.commit()
        conn.close()

        return redirect(url_for('lost_found'))

@app.route('/submit_found_item', methods=['POST'])
def submit_found_item():
    if request.method == 'POST':
        # Extract form data
        item_name = request.form['itemName']
        keywords = request.form['Keywords']
        date_found = request.form['dateFound']
        place_found = request.form['placeFound']
        reference_photo = request.files['referencePhoto']
        enrollment_no = session.get('enrollment_no')

        # Save reference photo to a folder and get its path
        photo_path = save_photo(reference_photo)

        # Insert data into the found_items table
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO found_items (item_name, keywords, date_found, place_found, reference_photo, enrollment_no)
                          VALUES (?, ?, ?, ?, ?, ?)''', (item_name, keywords, date_found, place_found, photo_path, enrollment_no))
        conn.commit()
        conn.close()

        return redirect(url_for('lost_found'))

@app.route('/notify', methods=['POST'])
def notify():
    enrollment_no = request.form['enrollment_no']
    # Implement notification mechanism here
    return 'Notification received successfully'

if __name__ == '__main__':
    app.run(debug=True)