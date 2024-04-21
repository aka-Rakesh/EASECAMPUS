import sqlite3
import hashlib

# Function to create the database table for students
def create_students_table():
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS students
                 (enrollment_no TEXT PRIMARY KEY,
                 name TEXT,
                 school TEXT,
                 course TEXT,
                 mobile_no INTEGER,
                 email TEXT,
                 password TEXT,
                 picture_path TEXT)''')
    
    conn.commit()
    conn.close()

# Function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to add a new student to the database
def add_student(input):
    conn = sqlite3.connect('easecampus.db')
    c = conn.cursor()
    (enrollment_no, name, school, course, mobile_no, email, password, picture_path) = input.split(',')
    hashed_password = hash_password(password)
    
    c.execute('''INSERT INTO students (enrollment_no, name, school, course, mobile_no, email, password, picture_path)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (enrollment_no, name, school, course, mobile_no, email, hashed_password, picture_path))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    #create_students_table()
    add_student(input())