import sqlite3

# Function to create the database table
def create_table():
    conn = sqlite3.connect('lost_and_found.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS lost_items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 description TEXT,
                 retrieved BOOLEAN)''')
    
    conn.commit()
    conn.close()

# Function to retrieve a lost item
def retrieve_lost_item(item_id):
    conn = sqlite3.connect('lost_and_found.db')
    c = conn.cursor()
    
    c.execute('''UPDATE lost_items
                 SET retrieved = TRUE
                 WHERE id = ?''', (item_id,))
    
    conn.commit()
    conn.close()

# Function to add a new lost item
def add_lost_item(name, description):
    conn = sqlite3.connect('lost_and_found.db')
    c = conn.cursor()
    
    c.execute('''INSERT INTO lost_items (name, description, retrieved)
                 VALUES (?, ?, FALSE)''', (name, description))
    
    conn.commit()
    conn.close()

# Function to retrieve all lost items
def get_lost_items():
    conn = sqlite3.connect('lost_and_found.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM lost_items''')
    items = c.fetchall()
    
    conn.close()
    return items

# Function to report or inquire about a lost item
def report_lost_item_inquiry(item_id):
    conn = sqlite3.connect('lost_and_found.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM lost_items
                 WHERE id = ?''', (item_id,))
    item = c.fetchone()
    
    conn.close()
    return item

if __name__ == '__main__':
    create_table()