
import sqlite3

#  Connected to SQLite database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

#  Created table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT
)
""")

# Inserted record (Parameterized Query)
def insert_student(name, age, course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", 
                   (name, age, course))
    conn.commit()
    print("Student inserted successfully.")

# Fetched records
def fetch_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\nStudent Records:")
    for row in rows:
        print(row)

# Updated record
def update_student(student_id, new_course):
    cursor.execute("UPDATE students SET course = ? WHERE id = ?", 
                   (new_course, student_id))
    conn.commit()
    print("Student updated successfully.")

#  Deleted record
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", 
                   (student_id,))
    conn.commit()
    print("Student deleted successfully.")

#  Menu Driven Program
while True:
    print("\n1. Insert Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        insert_student(name, age, course)

    elif choice == "2":
        fetch_students()

    elif choice == "3":
        student_id = int(input("Enter student ID to update: "))
        new_course = input("Enter new course: ")
        update_student(student_id, new_course)

    elif choice == "4":
        student_id = int(input("Enter student ID to delete: "))
        delete_student(student_id)

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")

# Closed connection properly
conn.close()
