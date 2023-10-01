#inputphase
qty = float(input("Quantity of widgets"))

#Process phase
if qty>10000:
  unitprice = 10.00
elif qty >= 5000:
  unitprice = 20.00
else:
  unitprice = 30.00

extprice = (qty * unitprice)
taxamt = (extprice * 0.07)
total = (extprice + taxamt)


print("Your extended price is:" , extprice)
print("Tax amount:" , taxamt)
print("The total is: " , total)


