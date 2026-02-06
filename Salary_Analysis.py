import matplotlib.pyplot as plt

employees = []
salaries = []

n = int(input("Enter number of employees: "))

for i in range(n):
    name = input(f"Enter name of employee {i+1}: ")
    salary = int(input(f"Enter salary of {name}: "))
    
    employees.append(name)
    salaries.append(salary)

# Plotting Salary Analysis
plt.plot(employees, salaries, marker='o')
plt.title("Employee Salary Analysis")
plt.xlabel("Employees")
plt.ylabel("Salary")
plt.grid(True)

plt.show()
