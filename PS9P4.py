def compticketprice(miles):
  if miles >= 30:
    ticketprice = 12
  elif 20 <= miles <= 29:
    ticketprice = 10
  elif 10 <= miles <= 19:
    ticketprice = 8
  else:
    ticketprice = 5
    
  return ticketprice

sumticketprice = 0.0
r = input("Do you want to compute the price of a train ticket? (y/n)")

while r == "y":
  lastname = input("Please enter your last name: ")
  miles = int(input("Enter the number of miles away from Chicago: "))
  ticketprice = compticketprice(miles)
  print(f"{lastname}'s ticket price to chicago is ${ticketprice}.")
  r = input("Do you want to compute the price of a train ticket? (y/n)")
  sumticketprice = sumticketprice + ticketprice
  
print(f"The total price of all tickets is ${sumticketprice}.")