#input phase
fixedcosts = float(input("Enter the fixed costs"))
PPU = float(input("Enter the price per unit"))
CPU = float(input("Enter the cost per unit"))

#process phase
breakpoint = (fixedcosts/PPU-CPU)

#output phase
print("Your break even point is", breakpoint)
