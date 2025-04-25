import mysql.connector

def init_db():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",       # Replace with your MySQL host
        user="root",           # Replace with your MySQL username
        password="PHW#84#JEOR",   # Replace with your MySQL password
        database="easy_travel" # Replace with your database name
    )
    cursor = conn.cursor()
    
    # Create table for trips
    cursor.execute('''CREATE TABLE IF NOT EXISTS trips (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      name VARCHAR(255), 
                      budget DECIMAL(10, 2))''')
    
    # Create table for suggestions (places & accommodations)
    cursor.execute('''CREATE TABLE IF NOT EXISTS suggestions (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      category VARCHAR(255), 
                      name VARCHAR(255), 
                      location VARCHAR(255))''')
    
    # Create table for necessities (hospitals, restaurants, grocery)
    cursor.execute('''CREATE TABLE IF NOT EXISTS necessities (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      type VARCHAR(255), 
                      name VARCHAR(255), 
                      address VARCHAR(255))''')
    
    # Create table for checklists
    cursor.execute('''CREATE TABLE IF NOT EXISTS checklist (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      trip_id INT,
                      item VARCHAR(255),
                      completed BOOLEAN,
                      FOREIGN KEY(trip_id) REFERENCES trips(id))''')
    
    # Create table for budget tracking
    cursor.execute('''CREATE TABLE IF NOT EXISTS budget (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      trip_id INT,
                      category VARCHAR(255),
                      amount DECIMAL(10, 2),
                      FOREIGN KEY(trip_id) REFERENCES trips(id))''')
    
    # Create table for customer reviews
    cursor.execute('''CREATE TABLE IF NOT EXISTS reviews (
                      id INT AUTO_INCREMENT PRIMARY KEY,
                      name VARCHAR(255), 
                      rating INT,
                      comment TEXT)''')
    
    # Commit changes and close connection
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")