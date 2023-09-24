#input phase
itemqty = float(input("Enter the item quantity"))

#Processing phase
if itemqty>= 1000:
    unitprice = 3.00
else:
  unitprice = 5.00

extprice = itemqty * unitprice
tax = extprice * 0.07
total = extprice + tax

#output phase
print("The item quantity is" , itemqty)
print("The unit price is" , unitprice)
print("The extended price will be" , extprice)
print("The tax amount will be" , tax)
print("The total is going to be" , total)