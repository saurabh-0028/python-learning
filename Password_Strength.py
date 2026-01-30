password = input("Enter your password: ")

length_ok = len(password) >= 8
has_upper = any(ch.isupper() for ch in password)
has_digit = any(ch.isdigit() for ch in password)
has_special = any(not ch.isalnum() for ch in password)

print("\n------ PASSWORD REPORT ------")

if length_ok:
    print("✔ Length OK")
else:
    print("✘ Password should be at least 8 characters")

if has_upper:
    print("✔ Uppercase present")
else:
    print("✘ Add at least one uppercase letter")

if has_digit:
    print("✔ Number present")
else:
    print("✘ Add at least one number")

if has_special:
    print("✔ Special character present")
else:
    print("✘ Add at least one special character")

if length_ok and has_upper and has_digit and has_special:
    print("\n  Strong Password")
else:
    print("\n Weak Password")
