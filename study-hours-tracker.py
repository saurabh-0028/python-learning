import matplotlib.pyplot as plt

def average(hours):
    return sum(hours) / len(hours)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
study_hours = []

for day in days:
    h = float(input(f"Enter study hours for {day}: "))
    study_hours.append(h)

avg = average(study_hours)

print("Average study hours:", avg)

# Visualization
plt.plot(days, study_hours, marker='o')
plt.axhline(avg, color='red', linestyle='--', label='Average')
plt.title("Weekly Study Hours Tracker")
plt.xlabel("Days")
plt.ylabel("Hours")
plt.legend()
plt.show()
