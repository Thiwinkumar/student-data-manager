import sqlite3

# Connect to database (or create it if it doesn't exist)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        roll_number TEXT NOT NULL UNIQUE,
        department TEXT NOT NULL
    )
''')
conn.commit()

# Add a student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    dept = input("Enter department: ")
    try:
        cursor.execute("INSERT INTO students (name, roll_number, department) VALUES (?, ?, ?)", (name, roll, dept))
        conn.commit()
        print("✅ Student added successfully!")
    except sqlite3.IntegrityError:
        print("❌ Roll number must be unique.")

# View all students
def view_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\n--- All Students ---")
    for student in students:
        print(student)

# Search student by roll number
def search_student():
    roll = input("Enter roll number to search: ")
    cursor.execute("SELECT * FROM students WHERE roll_number=?", (roll,))
    student = cursor.fetchone()
    if student:
        print("🎯 Student found:", student)
    else:
        print("❌ No student found with that roll number.")

# Delete student by roll number
def delete_student():
    roll = input("Enter roll number to delete: ")
    cursor.execute("DELETE FROM students WHERE roll_number=?", (roll,))
    conn.commit()
    print("🗑️ Student deleted (if existed).")

# Main loop
while True:
    print("\n=== Student Data Manager ===")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("👋 Exiting...")
        break
    else:
        print("Invalid option. Please try again.")
111111