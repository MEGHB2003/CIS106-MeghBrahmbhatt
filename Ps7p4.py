file = open("p4d.txt" , "r")

#initialize counters and sums to 0
C = 0.0
totextprice = 0.0

#get first data line
item = str(file.readline().rstrip('\n'))


while item != "":
  qty= float(file.readline())
  price = float(file.readline())
  
  extprice = qty * price
  #sum and count - in the loop 
  totextprice = totextprice + extprice
  C = C + 1

#display line of data
  print("The item is:" ,           item)
  print("The quantity is:" ,       qty)
  print("The price is:" ,          price)
  print("The extended price is:" , extprice)

  #get next data
  item = str(file.readline().rstrip('\n'))

# After the loop 
# final calculations 
# display them and sums and counts
print("Total extended price is:" ,   totextprice)
print("The number of orders are:" ,   C)
Avg = (totextprice / C)
print("Average extended price is:" ,  Avg)
