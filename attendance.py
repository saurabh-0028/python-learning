attendance = {}

def mark_attendance():
    emp_id = input("Enter Employee ID: ")
    status = input("Enter status (P/A): ").upper()

    if status == "P":
        attendance[emp_id] = "Present"
        print("Attendance marked: Present")
    elif status == "A":
        attendance[emp_id] = "Absent"
        print("Attendance marked: Absent")
    else:
        print("Invalid status")

def view_attendance():
    if not attendance:
        print("No attendance data available")
    else:
        print("\n--- Attendance Report ---")
        for emp, status in attendance.items():
            print("Employee ID:", emp, "| Status:", status)

def menu():
    print("\n--- Attendance Menu ---")
    print("1. Mark Attendance")
    print("2. View Attendance")
    print("3. Exit")

# Main Program Loop
while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        view_attendance()
    elif choice == "3":
        print("Exiting Attendance System")
        break
    else:
        print("Invalid choice")
