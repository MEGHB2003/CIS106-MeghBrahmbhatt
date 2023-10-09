totaldiscountamt = 0
response = input("Do you want to compute the final price? (Yes or No)")

while response == "Yes":
  qty = float(input("Enter the qtyof the item;"))
  priceofitem = float(input("Enter the price of the item:"))
  extprice = qty * priceofitem
  discount = 0.25 if extprice > 10000.00 else 0.10
  discountamt = discount * extprice
  totaldiscountamt = totaldiscountamt + discountamt
  total = extprice - discountamt

  print("Your extended price: " ,extprice)
  print("Discount amount: " , discountamt)
  print("Total amount will be " , total)
  response = input("Do you want to compute the final price? (Yes or No)")

print("Sum of all discounts:", totaldiscountamt)

  