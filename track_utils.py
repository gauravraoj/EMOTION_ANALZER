import sqlite3
import threading

# Thread-local storage for SQLite connection
thread_local = threading.local()

def get_db_connection():
    if not hasattr(thread_local, 'connection'):
        thread_local.connection = sqlite3.connect('data.db')
    return thread_local.connection

def create_page_visited_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')
    connection.commit()

def add_page_visited_details(pagename, timeOfvisit):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?, ?)', (pagename, timeOfvisit))
    connection.commit()

def view_all_page_visited_details():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM pageTrackTable')
    data = cursor.fetchall()
    return data

def create_emotionclf_table():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS emotionclfTable(rawtext TEXT, prediction TEXT, probability REAL, timeOfvisit TIMESTAMP)')
    connection.commit()

def add_prediction_details(rawtext, prediction, probability, timeOfvisit):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO emotionclfTable(rawtext, prediction, probability, timeOfvisit) VALUES (?, ?, ?, ?)', (rawtext, prediction, probability, timeOfvisit))
    connection.commit()

def view_all_prediction_details():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM emotionclfTable')
    data = cursor.fetchall()
    return data
