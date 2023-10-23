def detpayrate(jobcode):
    if jobcode == "L":
      return 25.0
    elif jobcode == "A":
      return 30.0
    elif jobcode == "J":
      return 50.0
    else:
      return 0.0
      
def calcgrosspay(hours, payrate):)
  if hours <= 40:
    return (40 * payrate) + ((hours - 40) * (payrate * 1.5))
  else:
    return hours * payrate


employees = []
totalgp = 0

while True:
    lanme = input("Enter last name")
  if name == "":
    break
  jobcode = input("Enter job code")
  hours = float(input("Enter hours worked"))
  payrate = detpayrate(jobcode)
  grosspay = calcgrosspay(hours, payrate)
  print("Gross pay:", grosspay)
  totalgp += grosspay
  employees.append((name, jobcode, hours, payrate, grosspay))



print("\nEmployee Data:")
for employee in employees:
  lname,grosspay = employee 
  print(f"Last name", lname), "Gross pay": grosspay
  
print("total of all gross pay ", totalgp)
