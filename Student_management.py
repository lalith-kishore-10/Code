import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="student_management"
    )

def add_student(name, age, course):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "INSERT INTO students (name, age, course) VALUES (%s, %s, %s)"
    values = (name, age, course)
    cursor.execute(sql, values)
    db.commit()
    print("Student added successfully!")
    db.close()

def view_students():
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    db.close()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Course: {student[3]}")

def update_student(student_id, name, age, course):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "UPDATE students SET name = %s, age = %s, course = %s WHERE id = %s"
    values = (name, age, course, student_id)
    cursor.execute(sql, values)
    db.commit()
    print("Student updated successfully!")
    db.close()

def delete_student(student_id):
    db = connect_to_db()
    cursor = db.cursor()
    sql = "DELETE FROM students WHERE id = %s"
    cursor.execute(sql, (student_id,))
    db.commit()
    print("Student deleted successfully!")
    db.close()

def menu():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            course = input("Enter student course: ")
            add_student(name, age, course)
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            course = input("Enter new course: ")
            update_student(student_id, name, age, course)
        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()