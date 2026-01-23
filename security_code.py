code1=int(input("Enter security code:"))
if code1==5566:
   dept=input("Enter your department Name:")
   if dept.lower()=="finance":
      level=int(input("Enter your access level:"))
      if level>=5:
        print("Access gurenteed: Welcome to the meeting Room.")
      else:
        print("insufficent access level")
   else:
    print("Access denied:Department not allow.")
else:
  print("Invalid security code.")