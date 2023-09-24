#input phase
item = (input("Enter item (A or B)"))
quantity = float(input("Enter qty of item"))

#process phase
if item== "A":
  unitprice = 10.00

else: 
  unitprice = 20.00

extprice = quantity + unitprice

print("Quantity ordered" , quantity)
print("unit price" ,unitprice)
print("extended price",extprice )

