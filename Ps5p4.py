#inputphase
notick = float(input("The Number of tickets you buy"))

#processphase

if notick>= 25.00:
  unitprice= 50.00
elif notick>=10:
  unitprice= 60.00
elif notick>=5:
  unitprice= 70.00
else:
  unitprice= 75.00

total= (notick * unitprice)

#outputphase
print("The number of tickets are:" , notick)
print("The price per ticket is:"  , unitprice)
print("The total cost will be:" ,  total)