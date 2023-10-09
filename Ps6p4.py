counter = 0
totalgrosspay = 0.0
response = input("Do you want to compute the gross pay (Yes or No)")

while response == "Yes":
  counter = counter + 1
  lastname = input("Enter the employees last name")
  hours = float(input("Enter hours worked"))
  rateofpay = float(input("Enter rate of pay"))
  grosspay = hours * (rateofpay * 1.5) if hours > 40 else hours *   rateofpay  
  totalgrosspay = totalgrosspay + grosspay
  print("Employee last name", lastname)
  print("Has a gross pay of", grosspay)
  response = input("Do you want to compute your gross pay? (Yes     or No)" )


averagepay = totalgrosspay/ counter
print("Amount of employees who entered in data:", counter)
print("The total gross pay is " , totalgrosspay)
print("Your average pay will be" , averagepay)