import sqlite3

# Function to create the database table for tickets
def create_tickets_table():
    conn = sqlite3.connect('ticket_generator.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS tickets
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 type TEXT,
                 enrollment_no INTEGER,
                 status BOOLEAN,
                 details TEXT)''')
    
    conn.commit()
    conn.close()

# Function to generate a new ticket
def generate_ticket(ticket_type, enrollment_no, details):
    conn = sqlite3.connect('ticket_generator.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO tickets (type, enrollment_no, status, details)
                 VALUES (?, ?, 'Open', ?)''', (ticket_type, enrollment_no, details))
    
    conn.commit()
    conn.close()

# Function to view all tickets
def view_tickets():
    conn = sqlite3.connect('ticket_generator.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM tickets''')
    tickets = c.fetchall()
    
    conn.close()
    return tickets

# Function to view tickets by student ID
def view_tickets_by_student(enrollment_no):
    conn = sqlite3.connect('ticket_generator.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM tickets WHERE student_id=?''', (enrollment_no,))
    tickets = c.fetchall()
    
    conn.close()
    return tickets

# Function to update ticket status
def update_ticket_status(ticket_id, status):
    conn = sqlite3.connect('ticket_generator.db')
    c = conn.cursor()
    
    c.execute('''UPDATE tickets SET status=?
                 WHERE id=?''', (status, ticket_id))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_tickets_table()
