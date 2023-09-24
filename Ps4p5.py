lastname = input("Enter last name")
grossincome = input("Enter gross income")
nod = input("Enter number of dependants")

adjgross = float(grossincome) - 12000.00 * float(nod)

if adjgross > 50000.00:
  tax = adjgross * 0.20
else:
  tax = adjgross * 0.10

if tax < 0:
  tax = 100.00

print("last name is" , lastname)
print("your gross income is $" , grossincome)
print("Number of dependants:" , nod)
print("Adjusted gross is:  $" , adjgross)
print("Income tax is: $" , tax)

