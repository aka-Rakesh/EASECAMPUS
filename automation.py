from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import sqlite3
import requests  # Import requests module

app = Flask(__name__)

# Function to scan for lost items and notify users
def scan_for_lost_items():
    print("Scanning for lost items...")
    conn = sqlite3.connect('easecampus.db')
    cursor = conn.cursor()

    # Query found items table
    cursor.execute('''SELECT * FROM found_items''')
    found_items = cursor.fetchall()
    #print("Found items:", found_items)

    # Query lost items table
    cursor.execute('''SELECT * FROM lost_items''')
    lost_items = cursor.fetchall()
    #print("Lost items:", lost_items)

    # Iterate through found items
    for found_item in found_items:
        # Check if item matches criteria with any lost item
        for lost_item in lost_items:
            #print("Checking found item:", found_item)
            #print("Checking lost item:", lost_item)
            # Compare the relevant attributes of found and lost items
            if (found_item[7] == 1 and lost_item[7] == 1 and  # Check status
                found_item[4] == lost_item[4] and  # Check place found vs place lost
                found_item[3] >= lost_item[3] and  # Check date found vs date lost
                len(set(found_item[2].split('#')) & set(lost_item[2].split('#'))) >= 2):  # Check keyword intersection
                # Send HTTP request to trigger notification
                trigger_notification(lost_item[6])
                break

    conn.close()
    print("Scan completed.")

# Function to trigger notification
def trigger_notification(enrollment_no):
    print(f"Notification sent to enrollment number: {enrollment_no}")
    # Send POST request to localhost:5000/notify with enrollment number as data
    response = requests.post('http://localhost:5000/notify', data={'enrollment_no': enrollment_no})
    if response.status_code == 200:
        print("Notification triggered successfully.")
        return True
    else:
        print("Failed to trigger notification.")
        return False

if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(scan_for_lost_items, 'interval', minutes=5)
    scheduler.start()
    #print("Scanning for lost items...\nScan completed.\nScanning for lost items...\nScan completed.")
    app.run(debug=True)
    #scan_for_lost_items()