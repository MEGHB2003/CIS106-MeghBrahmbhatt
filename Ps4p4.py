name = input("Enter name of appliance")
cost = float(input("Enter the cost of the appliance"))



if cost > 1000.00:
  warranty = cost * 0.10
else:
  warranty = cost * 0.05

total = (cost + warranty)


print("Appliance name", name)
print("Cost of appliance" , cost)
print("warranty cost", warranty)
print("total cost", total)