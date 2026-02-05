import matplotlib.pyplot as plt

subjects = ["Maths", "Science", "English", "Computer"]
marks = []

for sub in subjects:
    m = int(input(f"Enter marks for {sub}: "))
    marks.append(m)

plt.bar(subjects, marks)
plt.title("Student Marks Report")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
