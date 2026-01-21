emp_name=input("Enter employee name:")
basic_salary=int(input("Enter Basic salary:"))
bonus_amount=int(input("Enter Bonus amount:"))
tax_per=float(input("Enter tax in percentage:"))

gross_salary=basic_salary+bonus_amount
tax_amount=(gross_salary*tax_per)/100
net_salary=gross_salary-tax_amount

print("---------salary slip----------")
print("Employee name:",emp_name)
print("basic_salary:",basic_salary)
print("Gross salary:",gross_salary)
print("tax amount",tax_amount)
print("salary in hand",net_salary)