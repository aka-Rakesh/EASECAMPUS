import sqlite3

# Function to create the database table for exams
def create_exam_table():
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS exams
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 subject TEXT,
                 venue TEXT,
                 duration INTEGER,
                 date TEXT,
                 syllabus TEXT)''')
    
    conn.commit()
    conn.close()

# Function to create the database table for assignments
def create_assignment_table():
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS assignments
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 subject TEXT,
                 batch TEXT,
                 group_no TEXT,
                 start_date TEXT,
                 start_time TEXT,
                 end_date TEXT,
                 deadline TEXT,
                 filetype TEXT,
                 file_info TEXT)''')
    
    conn.commit()
    conn.close()

# Function to add a new exam
def add_exam(subject, venue, duration, date, syllabus):
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO exams (subject, venue, duration, date, syllabus)
                 VALUES (?, ?, ?, ?, ?)''', (subject, venue, duration, date, syllabus))
    
    conn.commit()
    conn.close()

# Function to add a new assignment
def add_assignment(subject, batch, group, start_date, start_time, end_date, deadline, filetype, file_info):
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO assignments (subject, batch, group, start_date, start_time, end_date, deadline, filetype, file_info)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (subject, batch, group, start_date, start_time, end_date, deadline, filetype, file_info))
    
    conn.commit()
    conn.close()

# Function to update exam information
def update_exam(exam_id, subject=None, venue=None, duration=None, date=None, syllabus=None):
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    update_query = '''UPDATE exams SET'''
    update_values = []

    if subject:
        update_query += ''' subject=?, '''
        update_values.append(subject)
    if venue:
        update_query += ''' venue=?, '''
        update_values.append(venue)
    if duration:
        update_query += ''' duration=?, '''
        update_values.append(duration)
    if date:
        update_query += ''' date=?, '''
        update_values.append(date)
    if syllabus:
        update_query += ''' syllabus=?, '''
        update_values.append(syllabus)

    # Remove the last comma and space
    update_query = update_query[:-2]
    
    update_query += ''' WHERE id=?'''
    update_values.append(exam_id)
    
    c.execute(update_query, update_values)
    
    conn.commit()
    conn.close()

# Function to update assignment information
def update_assignment(assignment_id, subject=None, batch=None, group=None, start_date=None, start_time=None, end_date=None, deadline=None, filetype=None, file_info=None):
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    update_query = '''UPDATE assignments SET'''
    update_values = []

    if subject:
        update_query += ''' subject=?, '''
        update_values.append(subject)
    if batch:
        update_query += ''' batch=?, '''
        update_values.append(batch)
    if group:
        update_query += ''' group=?, '''
        update_values.append(group)
    if start_date:
        update_query += ''' start_date=?, '''
        update_values.append(start_date)
    if start_time:
        update_query += ''' start_time=?, '''
        update_values.append(start_time)
    if end_date:
        update_query += ''' end_date=?, '''
        update_values.append(end_date)
    if deadline:
        update_query += ''' deadline=?, '''
        update_values.append(deadline)
    if filetype:
        update_query += ''' filetype=?, '''
        update_values.append(filetype)
    if file_info:
        update_query += ''' file_info=?, '''
        update_values.append(file_info)

    # Remove the last comma and space
    update_query = update_query[:-2]
    
    update_query += ''' WHERE id=?'''
    update_values.append(assignment_id)
    
    c.execute(update_query, update_values)
    
    conn.commit()
    conn.close()

# Function to view all submissions for an assignment
def view_assignment_submissions(assignment_id):
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM assignments WHERE id=?''', (assignment_id,))
    assignment = c.fetchone()
    
    conn.close()
    return assignment

# Function to mark assignments
def mark_assignment(assignment_id, marks):
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''UPDATE assignments SET marks=?
                 WHERE id=?''', (marks, assignment_id))
    
    conn.commit()
    conn.close()

# Function to push marks for exams
def push_exam_marks(exam_id, student_id, marks):
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''UPDATE exams SET marks=?
                 WHERE id=?''', (marks, exam_id))
    
    conn.commit()
    conn.close()

# Function to view existing exam info
def view_exam_info():
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM exams''')
    exams = c.fetchall()
    
    conn.close()
    return exams

# Function to view existing assignment info
def view_assignment_info():
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM assignments''')
    assignments = c.fetchall()
    
    conn.close()
    return assignments

if __name__ == '__main__':
    create_exam_table()
    create_assignment_table()
