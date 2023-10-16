f = open("prob3data.txt", "r")
sab = 0.0
lastname = f.readline()
while lastname !="":
  salary = float(f.readline())
  if salary >= 100000:
    bonusrate = 0.20
  else:
    if salary < 100000 and salary >=50000:
      bonusrate =0.15
    else:
      if salary < 50000:
         bonusrate = 0.10
  bonus = salary + bonusrate

  sab = sab + bonus
  print("lastname")
  
  