from sqlite3 import Connection
import sqlite3


db_conn = sqlite3.connect('pupil.db')
cursor = db_conn.cursor()
a = 'dsd'
try:
    cursor.execute("""CREATE TABLE students 
                (student_id INTEGER PRIMARY KEY, 
                first_name TEXT, 
                second_name TEXT, 
                country TEXT,    
                group_number TEXT, 
                birthday TEXT)
                """)
except sqlite3.Error:
    print('+')
try:
    cursor.execute("""CREATE TABLE marks
                   (mark_id TEXT PRIMARY KEY,
                   subject_name TEXT,
                   mark TEXT, 
                   time TEXT
                   """)
except sqlite3.Error:
    print('+')
student_id = 0
with open('pupil_list.csv', 'r') as text:
    line = text.readline()
    while line != '':
        student_id += 1
        line = line.split(',')
        line.insert(0, student_id)
        line.pop()
        try:
            cursor.execute("INSERT INTO students(student_id, first_name, second_name, country, group_number, birthday) "
                           "VALUES(?, ?, ?, ?, ?, ?)", line)
        except sqlite3.Error:
            print()
        line = text.readline()
    db_conn.commit()


