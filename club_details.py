import sqlite3

# Function to create the database table for club members
def create_club_members_table():
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS club_members
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 role TEXT,
                 picture TEXT,
                 email TEXT,
                 mobile_no TEXT)''')
    
    conn.commit()
    conn.close()

# Function to create the database table for events
def create_events_table():
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS events
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 date TEXT,
                 time TEXT,
                 registration_deadline TEXT,
                 venue TEXT,
                 prize TEXT,
                 info TEXT)''')
    
    conn.commit()
    conn.close()

# Function to add a new club member
def add_club_member(name, role, picture, email, mobile_no):
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO club_members (name, role, picture, email, mobile_no)
                 VALUES (?, ?, ?, ?, ?)''', (name, role, picture, email, mobile_no))
    
    conn.commit()
    conn.close()

# Function to edit club member details
def edit_club_member(member_id, name=None, role=None, picture=None, email=None, mobile_no=None):
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    update_query = '''UPDATE club_members SET'''
    update_values = []

    if name:
        update_query += ''' name=?, '''
        update_values.append(name)
    if role:
        update_query += ''' role=?, '''
        update_values.append(role)
    if picture:
        update_query += ''' picture=?, '''
        update_values.append(picture)
    if email:
        update_query += ''' email=?, '''
        update_values.append(email)
    if mobile_no:
        update_query += ''' mobile_no=?, '''
        update_values.append(mobile_no)

    # Remove the last comma and space
    update_query = update_query[:-2]
    
    update_query += ''' WHERE id=?'''
    update_values.append(member_id)
    
    c.execute(update_query, update_values)
    
    conn.commit()
    conn.close()

# Function to create a new event
def create_event(date, time, registration_deadline, venue, prize, info):
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO events (date, time, registration_deadline, venue, prize, info)
                 VALUES (?, ?, ?, ?, ?, ?)''', (date, time, registration_deadline, venue, prize, info))
    
    conn.commit()
    conn.close()

# Function to edit an existing event
def edit_event(event_id, date=None, time=None, registration_deadline=None, venue=None, prize=None, info=None):
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    update_query = '''UPDATE events SET'''
    update_values = []

    if date:
        update_query += ''' date=?, '''
        update_values.append(date)
    if time:
        update_query += ''' time=?, '''
        update_values.append(time)
    if registration_deadline:
        update_query += ''' registration_deadline=?, '''
        update_values.append(registration_deadline)
    if venue:
        update_query += ''' venue=?, '''
        update_values.append(venue)
    if prize:
        update_query += ''' prize=?, '''
        update_values.append(prize)
    if info:
        update_query += ''' info=?, '''
        update_values.append(info)

    # Remove the last comma and space
    update_query = update_query[:-2]
    
    update_query += ''' WHERE id=?'''
    update_values.append(event_id)
    
    c.execute(update_query, update_values)
    
    conn.commit()
    conn.close()

# Function to view registrations for an event
def view_event_registrations(event_id):
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM events WHERE id=?''', (event_id,))
    event = c.fetchone()
    
    conn.close()
    return event

# Function to view all club members
def view_club_members():
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM club_members''')
    members = c.fetchall()
    
    conn.close()
    return members

# Function to view all upcoming events
def view_upcoming_events():
    conn = sqlite3.connect('club_details.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM events''')
    events = c.fetchall()
    
    conn.close()
    return events

# Function to register for an event
def register_for_event(name, enrollment_no, mobile_no, email, additional_info):
    # Logic to handle registration for an event
    pass

if __name__ == '__main__':
    create_club_members_table()
    create_events_table()
