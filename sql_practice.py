from sqlite3 import Connection
import sqlite3


db_conn = sqlite3.connect('pupil.db')
cursor = db_conn.cursor()

try:
    cursor.execute("""CREATE TABLE subjects
                        (subject_id TEXT PRIMARY KEY,
                        teacher_name TEXT);
                        """)
except sqlite3.Error:
    print('+')

try:
    cursor.execute("""CREATE TABLE students 
                (student_id INTEGER PRIMARY KEY, 
                first_name TEXT, 
                second_name TEXT, 
                country TEXT,    
                group_number TEXT, 
                birthday INTEGER);
                """)
except sqlite3.Error:
    print('+')

try:
    cursor.execute("""CREATE TABLE marks
                (mark_id TEXT PRIMARY KEY,
                subject_id,
                student_id,
                mark TEXT,
                time INTEGER,
                FOREIGN KEY (student_id) 
                    REFERENCES students(student_id),
                FOREIGN KEY (subject_id)
                    REFERENCES subjects(subject_id));
                """)
except sqlite3.Error:
    print('+')


with open('subject_list.csv', 'r') as text:
    line = text.readline()
    while line != '':
        line = line.split(',')
        line.pop()
        try:
            cursor.execute("INSERT INTO subjects(subject_id, teacher_name) "
                           "VALUES(?, ?)", line)
        except sqlite3.Error:
            print('-')
        line = text.readline()
    db_conn.commit()

with open('pupil_list.csv', 'r') as text:
    line = text.readline()
    while line != '':
        line = line.split(',')
        line.pop()
        try:
            cursor.execute("INSERT INTO students(student_id, first_name, second_name, country, group_number, birthday) "
                           "VALUES(?, ?, ?, ?, ?, strftime('%s', ?))", line)
        except sqlite3.Error:
            print('1')
        line = text.readline()
    db_conn.commit()

with open('mark_list.csv', 'r') as text:
    line = text.readline()
    while line != '':
        line = line.split(',')
        line.pop()
        try:
            cursor.execute("INSERT INTO marks(mark_id, subject_id, student_id, mark, time) "
                           "VALUES(?, ?, ?, ?, strftime('%s', ?))", line)
        except sqlite3.Error:
            print()
        line = text.readline()
    db_conn.commit()
