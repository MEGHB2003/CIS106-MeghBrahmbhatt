def discount(qty,price,discrate):
  total = (qty * price)
  discamt = discrate * total 
  discprice = total - discamt 

  return discamt, discprice



qty = float (input("Enter the quantity "))
price = float(input("Enter the unit price"))
disrate = int(input("Enter the discount rate"))
discamt,discprice = discount(qty,price,disrate)

print("This is your qunatity: ", qty)
print("This is your price: ", price)
print("This is your discount rate: ", disrate)
print("This is your discounted price",discprice
