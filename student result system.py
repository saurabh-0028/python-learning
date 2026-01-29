def calculate_result(name, m1, m2, m3):
    total = m1 + m2 + m3
    percentage = total / 3

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "Fail"

    print("\n------ RESULT ------")
    print("Student Name :", name)
    print("Total Marks  :", total)
    print("Percentage   :", percentage)
    print("Grade        :", grade)


# Input Section
name = input("Enter Student Name: ")
m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))

# Function Call
calculate_result(name, m1, m2, m3)
