def otdprice(make, model, msrp, evc):
    percentoff = 0.0
    if make == "honda" and model == "accord":
      percentoff = 0.10
    elif make == "toyota" and model == "rav4":
      percentoff = 0.15
    elif evc == "y":
      percentoff = 0.30
    else:
      percentoff = 0.05

    discount = msrp * percentoff
    newmsrp = msrp - discount
    total = newmsrp * 1.07
    return total

summsrp = 0.0
sumsalesprice = 0.0
r = input("Do you want to run this program? (y/n)")

while r == "y":
  make = input("Enter the make of the car: ")
  model = input("Enter the model of the car: ")
  evc = input("Is it an electric vehicle? (y/n): ")
  msrp = float(input("Enter the MSRP of the car: "))
  total = otdprice(make, model, msrp, evc)
  print("The total cost of the car is: ", total)
  summsrp = summsrp + msrp
  sumsalesprice = sumsalesprice + total
  r = input("Do you want to run this program? (y/n)")
  
print("The total MSRP of all the cars is: ", summsrp)
print("The total sales price of all the cars is: ", sumsalesprice)