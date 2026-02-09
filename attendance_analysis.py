import matplotlib.pyplot as plt

def calculate_percentage(present, total_days):
    return (present / total_days) * 100

students = []
attendance_percent = []

n = int(input("Enter number of students: "))
total_days = int(input("Enter total working days: "))

for i in range(n):
    name = input(f"\nEnter name of student {i+1}: ")
    present = int(input(f"Enter days present for {name}: "))

    percent = calculate_percentage(present, total_days)

    students.append(name)
    attendance_percent.append(percent)

    if percent < 75:
        print("⚠ Warning: Low Attendance")

# Visualization
plt.bar(students, attendance_percent)
plt.axhline(75, color='red', linestyle='--', label='Minimum Required (75%)')
plt.title("Student Attendance Analysis")
plt.xlabel("Students")
plt.ylabel("Attendance Percentage")
plt.legend()
plt.show()
