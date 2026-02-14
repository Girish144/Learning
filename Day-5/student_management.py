# Day 5 Mini Project
# Student Management System

students = []

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age
    }

    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("❌ No students found.\n")
        return

    print("\n--- Student List ---")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']}")
    print()

def search_student():
    search_id = input("Enter Student ID to search: ")
    for student in students:
        if student["id"] == search_id:
            print(f"✅ Found: {student}")
            return
    print("❌ Student not found.\n")

def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.\n")

main()
