#Password Program
password=input("Enter your password :")

if password=="admin@1":
  print("Login successful")
else:
  print("Wrong Password")

# Email Validation
email = "user@example.com"
if "@" in email and "." in email:
      print("Valid Email")
else:
    print("Invalid Email")