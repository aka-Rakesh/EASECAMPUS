import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('easecampus.db')
c = conn.cursor()

# Create lost_items table
c.execute('''CREATE TABLE IF NOT EXISTS lost_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                keywords TEXT,
                date_lost DATE,
                place_lost TEXT,
                reference_photo TEXT,
                enrollment_no TEXT
            )''')

# Create found_items table
c.execute('''CREATE TABLE IF NOT EXISTS found_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                keywords TEXT,
                date_found DATE,
                place_found TEXT,
                reference_photo TEXT,
                enrollment_no TEXT
            )''')

# Function to add a lost item to the database
def add_lost_item(item_name, keywords, date_lost, place_lost, reference_photo, enrollment_no):
    c.execute('''INSERT INTO lost_items (item_name, keywords, date_lost, place_lost, reference_photo, enrollment_no)
                 VALUES (?, ?, ?, ?, ?, ?)''', (item_name, keywords, date_lost, place_lost, reference_photo, enrollment_no))
    conn.commit()

# Function to retrieve lost items from the database
def retrieve_lost_item(item_id):
    c.execute('''DELETE FROM lost_items WHERE id = ?''', (item_id,))
    conn.commit()

# Function to view all found items from the database
def view_found_items():
    c.execute('''SELECT * FROM found_items''')
    return c.fetchall()

# Close the database connection
conn.close()

if __name__ == '__main__':
    add_lost_item()
    #retrieve_lost_item()
    #view_found_items()