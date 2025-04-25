import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",    # Change if needed
        user="root",         # Your MySQL username
        password="PHW#84#jeor",  # Your MySQL password
        database="trip_planner"
    )
