def CompExtPrice(qty, unitprice):
  extprice = (qty * unitprice)

  if extprice > 10000:
    discamt = extprice *0.10
  else: 
    discamt = 0.0

  return extprice 

totalextprice = 0
R = input("Do you want to compute extended price (Y/N)")

while R == "Y":
  qty = float(input("Enter quantity: "))
  unitprice = float(input("Enter unit price: "))
  extprice = CompExtPrice(qty, unitprice)
  totalextprice = totalextprice + extprice
  print("Extended price is" , extprice)
  R = input("Do you want to compute extended price (Y/N):")

print("Total extended price is", totalextprice)

            
