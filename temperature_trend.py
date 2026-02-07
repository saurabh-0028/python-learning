import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temps = []

for day in days:
    t = int(input(f"Enter temperature for {day}: "))
    temps.append(t)

plt.plot(days, temps, marker='o')
plt.title("Weekly Temperature Trend")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()
