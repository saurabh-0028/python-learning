for i in range(3):
  p=int(input("Enter pin number:"))
  if (p==pin):
    print("correct pin")
    wb=int(input("Enter amount:"))
    if(cb>wb):
      cb=cb-wb
      print("Transection successful.")
    else:
      print("Insufficient balance")

    break
  else:
    print("Incorrect pin number")
else:

    print("card block")
