def squarefootage(length, width, height):
  totalsqrfoot = (2 * length * width) + (2 * length * height) + (2 * width * height)
  return totalsqrfoot

r = input("Do you wish to run this program? (y/n) ")
while r == "y":
  length = float(input("Enter the length of the room: "))
  width = float(input("Enter the width of the room: "))
  height = float(input("Enter the height of the room: "))
  print("The total square footage of the room is: ", squarefootage(length, width, height))
  gallonsneeded = squarefootage(length, width, height) / 50
  print("The total gallons of paint needed is: ", gallonsneeded)
  r = input("Do you wish to run this program again? (y/n) ")