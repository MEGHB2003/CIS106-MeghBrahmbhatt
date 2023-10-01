#input phase
principle = float(input("Enter the principle amount: "))
years = int(input("Enter years to maturity: "))

#processing phase
if principle > 100000 and years == 5:
  interestrate = 0.06
else:
  if principle >= 50000 or principle <= 100000 and years == 10:
    interestrate = 0.05
  else:
    if principle >= 50000 or principle <= 100000 and years == 5:
      interestrate = 0.04
    else:
      interestrate = 0.02
interestamnt = principle * interestrate

#output phase
print("The principle amount was: ", principle)
print("The interest rate: ", interestrate)
print("Interest amount for first year: ",interestamnt)